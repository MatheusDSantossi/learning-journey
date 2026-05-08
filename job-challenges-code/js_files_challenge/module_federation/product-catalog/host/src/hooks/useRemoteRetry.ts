import { useEffect, useState } from "react";
import { resetRemoteCircuit, subscribeToRemoteRecovery } from "../remotes/remoteHealth";
import { refreshRemote } from "../remotes/refreshRemote";

export function useRemoteRetry(scope: string) {
  const [retryToken, setRetryToken] = useState(0);

  useEffect(() => {
    const timer = setTimeout(() => {
      refreshRemote(scope);
      resetRemoteCircuit(scope);
      setRetryToken((t) => t + 1);
    }, 30_000);

    return () => clearTimeout(timer);
    //   subscribeToRemoteRecovery(scope, () => {
    //   setRetryToken((t) => t + 1);
    // });
  }, [scope, retryToken]);

  return retryToken;
}
