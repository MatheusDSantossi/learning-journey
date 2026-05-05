import { loadRemote } from "@module-federation/enhanced/runtime";
import { ComponentType, lazy } from "react";
import { withRemoteTelemetry } from "./telemetry";

export function loadTypedRemote<T extends ComponentType<any>>(scope: string) {
  return lazy(() =>
    withRemoteTelemetry(scope, () =>
      loadRemote(scope).then((mod) => ({
        default: ((mod as any).default ?? mod) as T,
      })),
    ),
  );
}
