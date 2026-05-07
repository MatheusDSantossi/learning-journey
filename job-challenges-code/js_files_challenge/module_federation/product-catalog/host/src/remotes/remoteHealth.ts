type RemoteHealthState = {
  failures: number;
  openUntil: number;
  lastError?: string;
};

type CircuitState = "CLOSED" | "OPEN" | "HALF_OPEN";

const circuits = new Map<
  string,
  {
    state: CircuitState;
    lastFailure: number;
  }
>();

const COOLDOWN = 30000;

const FAILURE_THRESHOLD = 2;
const OPEN_DURATION_MS = 30_000;

const states = new Map<string, RemoteHealthState>();
const listeners = new Map<string, Set<() => void>>();

function getState(scope: string): RemoteHealthState {
  if (!states.has(scope)) {
    states.set(scope, { failures: 0, openUntil: 0 });
  }

  return states.get(scope)!;

  //   const current = states.get(scope);
  //   if (current) return current;

  //   const initial: RemoteHealthState = {
  //     failures: 0,
  //     openUntil: 0,
  //   };

  //   states.set(scope, initial);

  //   return initial;
}

export function isCircuitOpen(scope: string) {
  const entry = circuits.get(scope);

  if (!entry) return false;

  if (entry.state === "OPEN") {
    const now = Date.now();

    if (now - entry.lastFailure > COOLDOWN) {
      // Move to HALF-OPEN
      entry.state = "HALF_OPEN";
      return false; // allow retry
    }
    return true;
  }
  return false;
}

export function recordRemoteSuccess(scope: string) {
  circuits.set(scope, {
    state: "CLOSED",
    lastFailure: 0,
  });
  //   states.set(scope, {
  //     failures: 0,
  //     openUntil: 0,
  //   });
}

export function recordRemoteFailure(scope: string, error: unknown) {
    circuits.set(scope, {
        state: "OPEN",
        lastFailure: Date.now()
    })
//   const state = getState(scope);
//   const failures = state.failures + 1;

//   if (failures >= FAILURE_THRESHOLD) {
//     const openUntil = Date.now() + OPEN_DURATION_MS;

//     states.set(scope, { failures, openUntil });

//     // Notify when cooldown ends
//     setTimeout(() => {
//       const ls = listeners.get(scope);
//       ls?.forEach((fn) => fn());
//     }, OPEN_DURATION_MS);
//   } else {
//     states.set(scope, { failures, openUntil: 0 });
//   }

  //   const nextFailures = state.failures + 1;
  //   const shouldOpen = nextFailures >= FAILURE_THRESHOLD;

  //   states.set(scope, {
  //     failures: nextFailures,
  //     openUntil: shouldOpen ? Date.now() + OPEN_DURATION_MS : 0,
  //     lastError: error instanceof Error ? error.message : String(error),
  //   });
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

export function getRemoteFallbackName(scope: string) {
  const [remoteName] = scope.split("/");
  return remoteName;
}
