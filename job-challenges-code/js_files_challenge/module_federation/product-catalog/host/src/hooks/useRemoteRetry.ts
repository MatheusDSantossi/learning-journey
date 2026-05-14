import { useEffect, useState } from "react";
import {
  getRemoteCircuit,
  resetRemoteCircuit,
  subscribeToRemoteHealth,
  subscribeToRemoteRecovery,
} from "../remotes/remoteHealth";
import { refreshRemote } from "../remotes/refreshRemote";

export function useRemoteRetry(scope: string) {
  const [retryToken, setRetryToken] = useState(0);

  useEffect(() => {
    let timer: ReturnType<typeof setTimeout> | undefined;

    const scheduleRetry = () => {
      if (timer) {
        clearTimeout(timer);
      }

      const circuit = getRemoteCircuit(scope);

      if (circuit.state === "CLOSED") {
        return;
      }

      const delay =
        circuit.state === "OPEN"
          ? Math.max(0, circuit.openUntil - Date.now())
          : 0;

      timer = setTimeout(() => {
        console.info("[useRemoteRetry] firing retry", {
          scope,
          retryToken,
        });
        refreshRemote(scope);
        setRetryToken((token) => token + 1);
      }, delay);
    };

    scheduleRetry();

    const unsubscribe = subscribeToRemoteHealth(scope, scheduleRetry);

    return () => {
      if (timer) {
        clearTimeout(timer);
      }

      unsubscribe();
    };
  }, [scope, retryToken]);

  return retryToken;
}
