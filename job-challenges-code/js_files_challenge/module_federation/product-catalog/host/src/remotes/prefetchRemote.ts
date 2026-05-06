import { loadRemote } from "@module-federation/enhanced/runtime";
import { withRemoteTelemetry } from "./telemetry";
import { isCircuitOpen } from "./remoteHealth";

export function prefetchRemote(scope: string) {
  if (isCircuitOpen(scope)) return;

  void withRemoteTelemetry(scope, () => loadRemote(scope)).catch(() => {
    // telemetry alreadt recorded the failure
  });
}
