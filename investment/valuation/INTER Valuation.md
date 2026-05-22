
| Metric                    | Latest value              | Period  | Quarterly or annualized               | Source                                               | Filing date |
| ------------------------- | ------------------------- | ------- | ------------------------------------- | ---------------------------------------------------- | ----------- |
| Revenue                   | 2,440,986 (R$ thousands)  | 1Q26    | Quarterly                             | Net revenues in the income statement, page 8         | 2026-05-06  |
| Net income                | 394,788 (R$ thousands)    | 1Q26    | Quarterly                             | Net income attributable to controllers, page 8       | 2026-05-06  |
| Tangible book value       | 1.5~                      | 1Q26    | Quarterly                             | Searched my self this approximated value             | 2026-05-21  |
| Total equity              | 10,413,730 (R$ thousands) | 1Q26    | Quarterly balance-sheet point-in-time | Balance sheet, page 7                                | 2026-05-06  |
| ROE                       | 15.5%                     | 1Q26    | Quarterly                             | Destaques 1T26                                       | 2026-05-06  |
| Loan portfolio            | 46,485,365 (R$ thousands) | 1Q26    | Quarterly balance-sheet point-in-time | Loans and advances to customers, net, page 7         | 2026-05-06  |
| NPL ratio                 | 4.7%                      | 1Q26    | Quarterly                             | NPL > 90 dias, Gráfico "Formação de NPL e Estágio 3" | 2026-05-06  |
| Efficiency ratio          | 43.8%                     | 1Q26    | Quarterly                             | Gráfico "Índice de Eficiência"                       | 2026-05-06  |
| CET1/Basel ratio          | 14,40%                    | 1Q26    | Quarterly                             | Searched it myself                                   | 2026-05-21  |
| Active clients            | 44.0 million              | 1Q26    | Quarterly                             | Management highlights, page 3                        | 2026-05-06  |
| Revenue per active client | R$ 57                     | 1Q26    | Quarterly                             | ARPAC Bruto Médio                                    | 2026-05-06  |
| Shares outstanding        | 441,488,373               | 1Q26    | Quarterly point-in-time               | Capital social table, page 49                        | 2026-05-06  |
| Current market cap        | 2,83 bilhões USD          | Current | Current market value                  | Searched it myself                                   | 2026-05-21  |
| Net interest margin       | 9.54%                     | 1Q26    | Quarterly                             | NIM 2.0                                              | 2026-05-06  |
| Cost of risk              | 5.1%                      | 1Q26    | Quarterly                             | Custo de Risco                                       | 2026-05-06  |

## Valuing Inter&Co: Methodology Framework for a High-Growth Fintech Bank

Inter&Co is a hybrid: it's a regulated Brazilian bank _and_ a high-growth super app with non-banking revenue streams (marketplace, insurance, investments, global accounts). That dual nature means no single methodology is sufficient — the right approach layers several models and stress-tests assumptions across them.

---

### What Metrics Actually Matter for Banks (Not Generic Corporates)

Before comparing methods, internalize that bank valuation uses fundamentally different metrics than industrial firms:

|Metric|Why It Matters for Banks|
|---|---|
|**ROE vs. Cost of Equity (COE)**|The engine of value creation. If ROE > COE, the bank creates value; if ROE < COE, it destroys it even while growing|
|**Tangible Book Value (TBV)**|The equity base from which returns are generated; the floor in stress scenarios|
|**Net Interest Margin (NIM)**|Spread between loan yields and funding costs — the core revenue driver|
|**Efficiency Ratio**|Operating expenses as % of revenue; critical for fintech where scale leverage is the thesis|
|**NPL / Coverage Ratio**|Non-performing loans and provisioning tell you the quality of the loan book|
|**CET1 Capital Ratio**|Regulatory capital; constrains growth capacity and dividend capacity|
|**Cost of Risk (CoR)**|Provisioning expense as % of loans; cycle-sensitive and credit quality signal|
|**Revenue per Active Client**|Fintech-specific: monetization of the user base beyond lending|
|**ARPAC (Avg Revenue Per Active Client)**|Inter's own KPI — measures cross-sell success across the super-app|

Free cash flow is **not** directly usable as in industrial DCF — you cannot separate operating from financing cash flows for a bank. Capital is the raw material of the business.

---
### The Five Methodologies: Deep Comparison

---
#### 1. Price-to-Book (P/B)

**Logic:** Bank value is anchored to the equity capital base. P/B compares market value to the book value of equity.

The fundamental driver of P/B is:

> **P/B = (ROE − g) / (COE − g)**

This means P/B is _not_ arbitrary — it's a direct function of ROE spread over cost of equity and the sustainable growth rate.

**For Inter&Co specifically:**

- Inter trades at a discount to U.S. neobank peers partly due to Brazil's higher COE (embedded country risk, BRL volatility) and partly because its ROE is still scaling
- Relevant comps: Nubank (NU), PagSeguro, StoneCo, and regional digital banks
- A P/TBV variant is preferable — tangible book strips out goodwill and intangibles that obscure lending capacity

**Strengths:**

- Directly anchored to capital, which is the correct base for banks
- Simple, market-observable, enables peer benchmarking
- Highly liquid comps exist in fintech

**Limitations:**

- Book value is an accounting construct — it reflects historical cost, not economic value
- Useless in isolation: a low P/B could mean deep value _or_ a bank destroying equity value (ROE < COE)
- Inter's technology platform and network effects carry significant off-balance-sheet value that P/B ignores entirely
- Accounting differences (IFRS 9 provisioning, capitalization policies) distort cross-border comparisons

**Verdict:** Necessary but insufficient. Always decompose P/B into its ROE/COE/g drivers rather than applying a multiple mechanically.

---

#### 2. Residual Income Model (RIM)

**Logic:** Value = Book Value + PV of all future "excess returns" (earnings above the equity charge).

> **Value = BV₀ + Σ [ (ROEₜ − COE) × BVₜ₋₁ ] / (1 + COE)ᵗ**

This is arguably the **most theoretically correct model for banks** because it explicitly models value creation relative to the cost of the capital base — which is precisely what banking economics is about.

**For Inter&Co specifically:**

- Inter is in an ROE ramp-up phase: currently ROE is below COE, so near-term residual income is negative
- The investment thesis rests on ROE crossing COE as scale is reached and the super-app cross-sell drives higher-margin non-lending revenue
- RIM makes this thesis explicit and quantifiable: when does the ROE inflection happen, and what does it imply for value?

**Strengths:**

- Theoretically rigorous — directly captures whether the bank is creating or destroying value
- Handles negative near-term earnings well (Inter is still building)
- Ties directly to observable accounting inputs (book value, ROE)
- Terminal value is more stable than in DCF because it anchors to book value

**Limitations:**

- Highly sensitive to COE assumption — and COE in Brazil is complex (CAPM with country risk premium, BRL/USD considerations for USD-listed ADR)
- Assumes clean-surplus accounting — requires adjustments for OCI items, FX translation reserves
- Requires multi-year ROE projections that are speculative for a rapidly evolving platform
- Book value can be manipulated through provisioning choices

**Verdict:** The strongest single methodology for Inter&Co. It forces explicit ROE trajectory modeling and ties value directly to capital efficiency.

---

#### 3. Gordon Growth Model (GGM) / Dividend Discount Model

**Logic:** Equity value = sustainable dividend (or distributable earnings) / (COE − g)

> **V = D₁ / (COE − g)**

For banks specifically, this is adapted as an **equity DDM** where you project dividends or capital returns, since banks cannot separate operating from financing cash flows.

**For Inter&Co specifically:**

- Inter does not currently pay meaningful dividends — it retains capital to fund growth
- GGM in its simple form is inapplicable at this stage
- A **multi-stage DDM** is more relevant: model an explicit high-growth phase with capital retention, transitioning to a mature phase with normalized payout ratios
- Brazilian banking regulation (BCB) constrains minimum capital ratios, which sets a floor on capital retention

**Strengths:**

- Theoretically sound for mature, dividend-paying banks
- Terminal value logic is clean and interpretable
- Forces discipline on sustainable payout capacity

**Limitations:**

- Completely inappropriate in single-stage form for Inter — no stable dividend, no mature payout policy
- Extremely sensitive to (COE − g) spread: small changes produce enormous valuation swings
- Growth rate _g_ must be ≤ nominal GDP growth in perpetuity — requires Brazil macro view
- Ignores the platform/super-app optionality entirely
- Payout ratios for a growth bank are endogenous (driven by capital needs), not exogenous inputs

**Verdict:** Useful only as a terminal value check within a multi-stage model, not as a standalone tool. Applying GGM to Inter today would systematically undervalue it.

---

#### 4. DCF — Equity Cash Flow / Dividend Discount Adapted for Banks

**Critical distinction:** You _cannot_ use a standard unlevered FCFF DCF for a bank. Debt is not a financing decision — it is the product. Instead, you discount **Free Cash Flow to Equity (FCFE)** or use an **excess capital return** framework.

**Bank-specific DCF logic:**

> **FCFE = Net Income − (Required Capital Increase)**
> 
> Where Required Capital Increase = (RWA growth) × (Target CET1 ratio)

This means the bank can only distribute earnings in excess of what's needed to support regulatory capital for growth. For Inter, which is growing its loan book aggressively, most earnings are being reinvested in capital — FCFE in the near term is minimal or negative.

**For Inter&Co specifically:**

- Model must be multi-stage: high growth (5–7 years), transition, and terminal
- Must track RWA growth explicitly — Inter's credit portfolio expansion consumes capital
- Non-banking revenue (marketplace, insurance, cross-border) has different capital intensity — deserves separate margin and growth assumptions
- BRL/USD dynamics matter for USD-denominated valuation: model in BRL, discount at BRL COE, then convert — do _not_ discount BRL cash flows at USD rates

**Strengths:**

- Most flexible — captures the full business model evolution
- Can model the super-app cross-sell revenue separately from NII
- Handles negative near-term FCFE in a high-growth phase appropriately
- Enables sensitivity analysis on the key value drivers (NIM, CoR, efficiency ratio, ARPAC)

**Limitations:**

- Terminal value typically represents 70–80%+ of total value for growth banks — the model is highly back-loaded
- COE is difficult to estimate robustly for Brazil: requires country risk premium (Damodaran's Brazil CRP is ~7–8%), size premium, and potential USD listing premium
- RWA projections require granular credit portfolio assumptions
- Garbage in, garbage out: the model's precision is illusory given macro uncertainty in Brazil

**Verdict:** Essential for articulating the investment thesis and running scenarios, but should be anchored by RIM and P/B to avoid unconstrained terminal value inflation.

---

#### 5. Sum-of-the-Parts (SOTP)

**Logic:** Value each business segment separately using the most appropriate methodology for that segment, then aggregate.

**For Inter&Co specifically, the natural segments are:**

|Segment|Methodology|Key Driver|
|---|---|---|
|**Core Banking / NII**|RIM or P/TBV|ROE, NIM, CoR|
|**Credit Portfolio**|P/Loan or RWA multiple|Credit quality, NPL|
|**Inter Shop (marketplace)**|EV/GMV or EV/Revenue|GMV growth, take rate|
|**Inter Invest (brokerage/AM)**|AUM multiple or P/Revenue|AUM growth, fee yield|
|**Inter Seguros (insurance)**|P/E or EV/GWP|Combined ratio, growth|
|**Global Account / US operations**|EV/Revenue or DCF|Customer growth, monetization|

**Strengths:**

- Captures the conglomerate discount/premium — Inter's platform businesses trade at tech multiples, not bank multiples
- Forces explicit assumptions about each segment's profitability and capital intensity
- Reveals where value is actually being created (likely marketplace + investments, not just lending)
- Directly comparable to Nubank's segment reporting and XP's asset management business

**Limitations:**

- Segment-level financials are not fully disclosed by Inter — requires estimates and allocations
- Shared costs (technology, compliance, customer acquisition) are difficult to allocate correctly
- Risk of double-counting synergies (the super-app thesis _is_ the synergy between segments)
- Cross-segment capital allocation is subjective
- Can produce a "parts exceed the whole" result that isn't realizable in practice

**Verdict:** Highly valuable for Inter specifically, precisely because the market may be misvaluing it purely as a bank. SOTP can reveal the embedded technology/platform optionality. Use as a cross-check and bull-case framework.

---
### Recommended Analytical Framework for Inter&Co

Rather than picking one method, layer them:

**Primary:** Residual Income Model — because it correctly frames the ROE/COE inflection thesis that drives the entire investment case

**Secondary:** Equity FCFE DCF — to model the path of capital generation and stress-test macro scenarios (Selic rate, BRL, Brazilian credit cycle)

**Cross-check:** P/TBV decomposition — to anchor to market comparables (Nubank, regional digital banks) and verify the implied ROE/COE spread is realistic

**Upside framing:** SOTP — to quantify what the platform businesses are worth independently and test whether the market is appropriately crediting Inter for being more than a bank

**Terminal value sanity check:** GGM inputs — ensure your terminal growth rate and payout ratio assumptions are internally consistent with Brazilian nominal GDP and regulatory capital requirements

The core question in any Inter&Co valuation is not "what multiple does it trade at?" but rather: **at what point does ROE sustainably exceed COE, and how large is the capital base when that happens?** Every methodology above is ultimately answering that question from a different angle.

![[inter_co_valuation_scenarios.html]]

Here's the full context behind the numbers:

**Inter&Co starting point (Q1 2026).** Inter achieved record net income of R$395 million in Q1 2026, up 38% year-over-year, with ROE at 15.5% and ROTE near 20%. The efficiency ratio declined to 43.8% from 62.4% two years earlier, and total expenses of R$996 million grew 20% year-over-year, well below the 33% revenue growth rate — the hallmark of operating leverage finally firing. However, NPLs rose to 5.1% from 4.7%, with private payroll growth and credit cards as the main contributors, alongside macro pressures as system delinquency rises. [Quartr + 2](https://quartr.com/companies/inter-co-inc_14505)

**Why these scenario ranges are calibrated where they are:**

On the conservative side, loan growth of 18–22% reflects a scenario where the credit cycle deteriorates further and Inter deliberately slows origination — consistent with management guidance of 25–30% loan growth in 2025, which would represent a floor if conditions worsen. The ROE ceiling at 18% reflects a stall in the ROE-over-COE inflection if NPLs persist above 5%. [StockAnalysis](https://stockanalysis.com/stocks/intr/)

The base case (25–30% loan growth, ROE 20–23%) tracks management guidance with the assumption that private payroll and FGTS-backed products improve the credit mix. The gross loan portfolio grew 33% year-over-year to R$50 billion, outpacing the Brazilian market by over 3x — the base case assumes that gap narrows modestly as Inter's loan book matures. [Stocktitan](https://www.stocktitan.net/sec-filings/INTR/6-k-inter-co-inc-current-report-foreign-issuer-45c4e26eda0a.html)

The aggressive case (32–38% loan growth, ROE 25–28%) requires Inter to execute fully on the super-app monetization thesis. The reference point is Nubank, where an all-time high net income of $895 million and ROE of 33% were achieved in FY2025, reflecting the ability to combine disciplined growth with sustained profitability. [sec](https://www.sec.gov/Archives/edgar/data/0001691493/000129281426000501/nu20260225_6k.htm)

**Peer context.** Itaú sits as the maturity benchmark: Itaú delivered recurring managerial profit of R$46.8 billion in 2025, up 13.1%, with ROE of 23.4% and the 90-day NPL ratio at 1.9%, the best historical level for individuals in Brazil. The NPL gap between Itaú (1.9%) and Inter (5.1%) is almost entirely explained by credit mix — Itaú's book is far more corporate and payroll-heavy, which Inter is actively shifting toward. BTG represents the high-ROE efficiency benchmark: BTG achieved a record ROE of 26.9% for 2025, with revenue growth of 32% and net income growth of 35% year-over-year. Mercado Pago shows what hyper-growth looks like when ecosystem leverage is prioritized over credit quality: the Mercado Pago credit portfolio nearly doubled year-over-year to $12.5 billion, and assets under management reached close to $19 billion, growing at 78% year-over-year. [stocktitan + 2](https://www.stocktitan.net/sec-filings/ITUB/6-k-itau-unibanco-holding-s-a-current-report-foreign-issuer-a9f0b01efccc.html)

The tabs in the dashboard walk through the full scenario grid, ROE/net income trajectory charts, the peer positioning bubble map, and the six key risk factors that determine which scenario materializes.

![[inter_co_valuation_scenarios 1.html]]

**Cost of equity build-up.** Damodaran's January 2026 table shows Brazil at a Ba1 Moody's rating, with an adjusted default spread of 2.13%, a country risk premium of 3.24%, and a total equity risk premium of 7.47%. On top of that I stack: a US risk-free rate of 4.40%, a beta of 1.20 (fintech banks are structurally more volatile than incumbents — Nubank's public beta runs 1.15–1.25), and a 1.50% size/illiquidity premium for Inter's smaller float vs Itaú. That yields **Ke (USD) ≈ 14.86%**. Converting to BRL nominal using Fisher parity with Brazilian CPI at ~5.5% and US CPI at ~2.5% produces a **base Ke of 18%** in BRL terms — which is internally consistent with the currency in which Inter's equity book is denominated. Importantly, Damodaran himself notes that for currencies like the Brazilian real, it is more prudent to do calculations entirely in US dollars and convert using the differential inflation rate.

**ROE path.** The model fades ROE from the Q1 2026 reported **15.5%** to **21%** by year 5. That is disciplined: it is below Itaú's current 23.4% and well below Nubank's 33%, reflecting Inter's smaller scale and higher consumer credit risk. The key driver of the fade is continued operating leverage (efficiency ratio tracking toward the low-40s) and credit mix improvement toward FGTS/payroll products that carry lower cost of risk.

**What the three sensitivity tables tell you:**

The ROE × Ke table (Sensitivity 1) is the most critical. At the base case (ROE 21%, Ke 18%), the model produces a meaningful premium to the ~$6.40 market price. The valuation only falls below current market prices in scenarios where Ke pushes above 20% and terminal ROE stays stuck below 18% — that is, where Brazil country risk widens materially AND Inter's operating model fails to improve. The g × Ke table (Sensitivity 2) shows that the long-term growth assumption matters less than the ROE/Ke spread: even at g = 5% (implying slower-than-nominal-GDP perpetuity), the base-case ROE trajectory still yields positive upside. The interactive tab lets you stress any combination live.

**Critical limitation to flag:** terminal value represents roughly 65–75% of total intrinsic value across most scenarios — this is normal for high-growth banks in the RIM framework, but it means the output is highly sensitive to what you believe about steady-state ROE and the permanence of the COE-spread. The book value anchor (R$10.4B, roughly $1.81B) provides a hard floor.