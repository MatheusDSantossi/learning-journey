import { useEffect, useState } from "react";
import { subscribeToRemoteRecovery } from "../remotes/remoteHealth";


export function useRemoteRetry(scope: string) {
  const [retryToken, setRetryToken] = useState(0);

  useEffect(() => {
    return subscribeToRemoteRecovery(scope, () => {
      setRetryToken((t) => t + 1);
    });
  }, [scope]);

  return retryToken;
}
