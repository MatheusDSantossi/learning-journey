# Line by line explanation

CREATE OR REPLACE FUNCTION example(parameter text) -> defines a function named exmaple taking a text argument.

---

RETURNS numeric -> function returns PostgreSQL numeric (arbitrary precision decimal)

---

LANGUAGE 'plpgsql' -> implemented in PL/pgSQL (server procedural language).

---

COST 100 -> planner cost estimate for calling function (default for non-SQL functions); rarely needed to set manually.

---

VOLATILE PARALLEL UNSAFE -> declares function volatility and parallel-safety attributes:

- **VOLATILE**: means the function can return different results even in same transaction (most permissive). This prevents certain planner optimizations.
  
- **PARALLEL UNSAFE**: prevents the function from being called in parallel worker processes.

DECLARE parameter_value numeric := 0.0; -> local variable initialized to 0.0.

SELECT COALESCE(TABLE_VALUE::numeric, 0.0) INTO parameter_value FROM TABLE WHERE D_E_L_E_T_E = FALSE AND TABLE_PARAM = parameter; -> queries table 'TABLE' for the row(s) matching TABLE_PARAM = parameter and WHERE D_E_L_E_T_E = FALSE, converts TABLE_VALUE to numeric and coalesces null to 0.0, storing result into the local variable.

RETURN parameter_value; -> returns the value

# Concepts involved / why it's written thta way

- **Parameter-table pattern**: This is a standard approach to store configuration/value pairs in a table keyed by a name (param).
- **Soft-delete flag**: D_E_L_E_T_E indicates whether a row is "deleted" without physically removing it.
- **Type casting**: TABLE_VALUE::numeric converts stored text/string value to nmeric.
- **Null handling**: COALESCE(..., 0.0) ensures a numeric default when underlying value is NULL.
- **PL/pgSQL vs SQL function**: Author chose PL/pgSQL (procedural), probably for familiarity or future expansion, but the function is a single SELECT so SQL-language function could be simpler and faster.
**- Volatility/Parallel attributes**: They affect planner behavior, likely miss-declared here (see below)

# Problems, concers & code quality assessment

1. **VOLATILE PARALLEL UNSAFE is probably wrong**:
    - The function only reads from a table; it's deterministic for the same DB state. It should be *STABLE* (safe: returns same result within a single statement) or at least not need *VOLATILE*. Making *VOLATILE* disables optimizer opportunities and can prevent using parallel query exectuion.
    - *PARALLEL UNSAFE* combined with *VOLATILE* blocks parallelism. If the function is purely a *SELECT* with no side effects, it can be *PARALLEL SAFE* (if the underlying operations are safe).
2. **SELECT INTO can fail on multiple rows**:
    - If more than one row matches, the *SELECT INTO* will raise *TOO_MANY_ROWS* error. The code assumes *TABLE_PARAM* is unique. If it's not guaranteed unique, you need LIMIT 1 or aggregation or make *TABLE_PARAM* UNIQUE.
3. No **LIMIT** or explicit uniqueness check:
    - As above, ambiguity whether parameter names are unique
4. **Indexing / performance**:
   - If *TABLE* is big and calls are frequent, there must be an index on *TABLE_PARAM* (possibly a partial index WHERE D_E_L_E_T_E = FALSE) to avoid sequential scans.
5. **Type-safety**:
   - *TABLE_VALUE::numeric* casts the stored value; if the column is already nuumeric, cast is redundant, if it's text that may contain non-numeric values, the cast may raise *invalid_text_representation* errors. No error handling is present.
6. **Handling of D_E_L_E_T_E**:
   - Compares *D_E_L_E_T_E = FALSE* if *D_E_L_E_T_E* is nullable, rows with NULL will be excluded because NULL = FALSE is unknown. If intent is to treat null as not-deleted, use COALESCE(D_E_L_E_T_E, FALSE) = FALSE or not COALESCE(D_E_L_E_T_E, FALSE).
7. **Return type not constrained**:
   - *RETURNS numeric* with no precision/scales specified is flexible but sometimes we want *numeric(18, 2)* for money. Using numeric is fine, but we might consider specificity if this is a monetary value.
8. **Privilege/security atributes**:
   - Default is *SECURITY INVOKER*. If used in contexts with different privileges, think about *SECURITY DEFINER (dangerous)* or ensure proper grants on table.
9. **Use of PL/pgSQL for trivial query**:
    - A simple SELECT-only function performs better and is simpler if defined as LANGUAGE SQL. PL/pgSQL adds overhead.
10. **No input validation**:
    - *parameter* could be NULL, function will compare TABLE_PARAM = NULL which returns no rows. Possibly return 0. Consider early *IF parameter IS NULL THEN RETURN 0; END IF*.
    
# Security risks

- **SQL injection**: Not an issue as written, no dynamic SQL is used. Using variable in the WHERE clause in PL/pgSQL is safe.
- *Privilege escalations*: If we change to *SECURITY DEFINER*, we need to be **careful**: this can expose table data to unprivileged users.
- **Error information leakage**: If *TABLE_VALUE* may contain non-numeric strings, a cast error could buble up. Consider handling exceptions and returning a safe default.

# Performance & scalability

- Single-row index lookup (on *TABLE_PARAM*) is cheap; ensure index exists.
- For many concurrent reads if config parameters, a DB function call each time is OK but repeated calls from many request may be slower than caching at app layer or using *pg_prewarn/in-memory* caches (Redis, in-process).
- The numeric type is slower than interger/double precision for heavy math; choose type according to domain needs.
- **VOLATILE / PARALLEL UNSAFE** prevents parallel query optimization, switch to *STABLE / PARALLEL SAFE* where correct.

# Suggested improvements (concrete)

## A. Minimal, safer PL/pgSQL refactor

```SQL
CREATE OR REPLACE FUNCTION example(parameter text)
RETURNS numeric
LANGUAGE plpgsql
STABLE
PARALLEL SAFE
AS $$
DECLARE
    parameter_valeu numeric := 0;
BEGIN
    IF parameter IS NULL THEN
        RETURN 0;
    END IF;

    SELECT TABLE_VALUE::numeric
    INTO parameter_value
    FROM TABLE
    WHERE COALESCE(D_E_L_E_T_E, FALSE) = FALSE
        AND TABLE_PARAM = parameter
    LIMIT 1;

    RETURN COALESCE(parameter_value, 0);
EXCEPTION WHEN invalid_text_representation THEN
    -- If the stored value can't be converted to numeric, return default (or raise) 
    RETURN 0;
END;
$$;
```

### Changes made:

- *STABLE* and *PARALLEL SAFE*, allow planner optimizations and parallel workers.
- *COALESCE(D_E_L_E_T_E, FALSE)*, treats NULL as not deleted.
- *LIMIT 1* prevents *TOO_MANY_ROWS*.
- input NULL check.
- Exception handling for invalid text -> numeric cast

## B. Simpler SQL language function (recommended for single SELECT)

if the function is simply returning a single value, a SQL function is simpler and faster:

```SQL
CREATE OR REPLACE FUNCTION example(parameter text)
RETURNS numeric
LANGUAGE SQL
STABLE
PARALLEL SAFE
AS $$
    SELECT COALESCE( (TABLE_VALUE::numeric), 0.0)
    FROM TABLE
    WHERE COALESCE(D_E_L_E_T_E, false) = false
        AND TABLE_PARAM = $1
    LIMIT 1;
$$;
```

- SQL functions have less overhead and the planner can inline them sometimes.
- *$1* is the first argument in SQL-language functions.

## C. Index recommendation

if most lookups are by TABLE_PARAM and only non-deleted rows are relevant:

```SQL
CREATE UNIQUE INDEX IF NOT EXISTS idx_table_param_not_delted
ON TABLE (TABLE_PARAM)
WHERE COALESCE(D_E_L_E_T_E, false) = false;
```

- If *TABLE_PARAM* should be unique (per active row), make it a unique index.
- Partial index improves lookup performance and index size.

## D. Schema suggestions

- Ensure *D_E_L_E_T_E* is BOOLEAN (not text), default FALSE, NOT NULL if possible.
- If TABLE_VALUE is numeric-like data (money/numbers), store as *numeric* (or *numeric(scale, precision)* or *double precision* depending on needs) rather than text. Eliminates casting and errors.

# Extra best-practices & architecture suggestions

- If this table stores application configuration parameters that are read frequently and rarely changed, consider caching them at app level (e.g., per-process in-memory cache or Redis) and invalidate on cahnges.
- Use a small, well-typed schema for parameters: key (text, PK), **value_numeric** (numeric), value_text, updated_at; typed columns reduce casting problems. 
- For multi-tenant systems, keys might need a tenant_id in the WHERE clause; design indexes accordingly.
- Add monitoring/metrics if reads are heavy (count calls, response time).
- Add unit tests for function behaviour, valid numeric, null, multiple rows, non-numeric stored value.

# When to choose numeric vs double precision

- **numeric** for exact decimals (money, financial data).
- **double precision** (floating point) for scientific/calculation where approximate floats are OK and performance matters.

# Suggested follow-up topics to study

- PostgreSQL function volatility: **IMMUTABLE**, **STABLE**, **VOLATILE** and **PARALLEL** safety.
- PL/pgSQL vs SQL-language functions: pros/cons and performance differences.
- Indexing strategies (partial indexes, expression indexes, covering indexes).
- Soft-delete patterns and their tradeoffs (partial indexes / filtered queries).
- Error handling in PL/pgSQL and defensive ocding in DB functions.
- **Data typing**: when to use *numeric* vs *int* vs *double precision*,
- Caching strategies for configuration data (application cache, Redis, etc).
- Security: SECURITY INVOKER vs SECURITY DEFINER and least-privilege patterns.
- Testing database functions (pgTAP or integration tests).

# Real-world scenarios where this pattern is used

- Application configuration retrieval (max_discount, tax_rate).
- Feature flags stored in DB read by many services.
- Tenant-specific parameters in multi-tenant apps.
- Financial settings like interest rates or thresholds.

# Small reflection questions (for us)

1. Is TABLE_PARAM supposed to be unique? If yes, can we enforce it at schema level?

2. Is TABLE_VALUE currently stored as text or numeric in your DB? (If text, are non-numeric values possible?)

3. How often is this function called in production? (per-request or rare admin reads?)

4. Do you have many such parameter lookups? Would a centralized typed table be better?
