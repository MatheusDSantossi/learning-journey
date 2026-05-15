type RemoteHealthState = {
  failures: number;
  openUntil: number;
  lastError?: string;
};

type CircuitState = "CLOSED" | "OPEN" | "HALF_OPEN";

type CircuitEntry = {
  state: CircuitState;
  failures: number;
  openUntil: number;
  lastError?: string;
};

const COOLDOWN_MS = 30_000;

const FAILURE_THRESHOLD = 2;
const OPEN_DURATION_MS = 30_000;

// const states = new Map<string, RemoteHealthState>();
const circuits = new Map<string, CircuitEntry>();
const listeners = new Map<string, Set<() => void>>();

function ensureCircuit(scope: string): CircuitEntry {
  let circuit = circuits.get(scope);

  if (!circuit) {
    circuit = {
      state: "CLOSED",
      failures: 0,
      openUntil: 0,
    };

    circuits.set(scope, circuit);
  }

  return circuit;
}

function notify(scope: string) {
  listeners.get(scope)?.forEach((callback) => callback());
}

/**
 * Returns true only while the circuit is still open and the cooldown has not expired.
 * If the cooldown expires, the circuit moves to HALF_OPEN and the next load is allowed.
 */
export function isCircuitOpen(scope: string) {
  const circuit = ensureCircuit(scope);
  const now = Date.now();

  if (circuit.state !== "OPEN") {
    return false;
  }


  if (now < circuit.openUntil) {
    return true
  }

  if (now >= circuit.openUntil) {
    // Move to HALF-OPEN
    circuit.state = "HALF_OPEN";
    notify(scope);
    return false; // allow retry
  }
  
  return true;
}

export function recordRemoteSuccess(scope: string) {
  const circuit = ensureCircuit(scope);

  circuit.state = "CLOSED";
  circuit.failures = 0;
  circuit.openUntil = 0;
  delete circuit.lastError;

  notify(scope);
}

export function recordRemoteFailure(scope: string, error: unknown) {
  const circuit = ensureCircuit(scope);

  circuit.state = "OPEN";
  circuit.failures += 1;
  circuit.openUntil = Date.now() + COOLDOWN_MS;
  circuit.lastError = error instanceof Error ? error.message : String(error);

  notify(scope);
}

export function subscribeToRemoteHealth(scope: string, callback: () => void) {
  if (!listeners.has(scope)) {
    listeners.set(scope, new Set());
  }

  listeners.get(scope)!.add(callback);

  return () => {
    listeners.get(scope)?.delete(callback);
  };
}

export function subscribeToRemoteRecovery(scope: string, callback: () => void) {
  if (!listeners.has(scope)) {
    listeners.set(scope, new Set());
  }

  listeners.get(scope)!.add(callback);

  return () => {
    listeners.get(scope)?.delete(callback);
  };
}

export function resetRemoteCircuit(scope: string) {
  circuits.delete(scope);
}

export function getRemoteFallbackName(scope: string) {
  return scope.split("/")[0];
}

export function getRemoteCircuit(scope: string): CircuitEntry {
  return ensureCircuit(scope);
}

/**
 * Optional manual escape hatch.
 * Not part of normal retry flow.
 */
export function forceRemoteRetry(scope: string) {
  const circuit = ensureCircuit(scope);

  circuit.state = "HALF_OPEN";
  circuit.openUntil = 0;

  notify(scope);
}
