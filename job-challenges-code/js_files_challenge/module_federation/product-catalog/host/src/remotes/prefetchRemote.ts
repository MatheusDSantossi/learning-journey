import { loadRemote } from "@module-federation/enhanced/runtime";
import { withRemoteTelemetry } from "./telemetry";

export function prefetchRemote(scope: string) {
  void withRemoteTelemetry(scope, () =>
    loadRemote(scope).catch((error) => {
      console.debug(`[prefetchRemote] failed for ${scope}`, error);
    }),
  );
}
