import { loadRemote } from "@module-federation/enhanced/runtime";

export function prefetchRemote(scope: string) {
  void loadRemote(scope).catch((error) => {
    console.debug(`[prefetchRemote] failed for ${scope}`, error);
  });
}
