import { loadRemote } from "@module-federation/enhanced/runtime";
import { ComponentType, lazy } from "react";

export function loadTypedRemote<T extends ComponentType<any>>(scope: string) {
  return lazy(() =>
    loadRemote(scope).then((mod) => ({
      default: ((mod as any).default ?? mod) as T,
    })),
  );
}
