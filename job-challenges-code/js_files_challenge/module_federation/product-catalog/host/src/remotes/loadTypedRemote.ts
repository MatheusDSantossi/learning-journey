import { loadRemote } from "@module-federation/enhanced/runtime";
import { ComponentType, lazy } from "react";
import { withRemoteTelemetry } from "./telemetry";
import {
  getRemoteFallbackName,
  isCircuitOpen,
  recordRemoteFailure,
  recordRemoteSuccess,
} from "./remoteHealth";
import remoteFallbacks from "./remoteFallbacks";

export function loadTypedRemote<T extends ComponentType<any>>(scope: string) {
  return lazy(async () => {
    if (isCircuitOpen(scope)) {
      const fallbackName = getRemoteFallbackName(scope);
      const FallbackComponent = remoteFallbacks[scope];

      if (FallbackComponent) {
        return { default: FallbackComponent as T };
      }

      throw new Error(
        `[CircuitBreaker] Remote "${fallbackName}" is temporarily unavailable`,
      );
    }

    try {
      const mod = await withRemoteTelemetry(scope, () => loadRemote(scope));
      recordRemoteSuccess(scope);

      return {
        default: ((mod as any).default ?? mod) as T,
      };
    } catch (error) {
      recordRemoteFailure(scope, error);

      const FallbackComponent = remoteFallbacks[scope];

      if (FallbackComponent) {
        return { default: FallbackComponent as T };
      }

      throw error;
    }
  });
}
