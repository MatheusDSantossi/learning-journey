import { registerRemotes } from "@module-federation/enhanced/runtime";

type Manifest = Record<string, { entry: string; version: string }>;

declare global {
  interface Window {
    __REMOTE_MANIFEST__?: Manifest;
    __REMOTE_REFRESH_TOKENS__?: Record<string, number>;
  }
}

export function refreshRemote(scope: string) {
  const [name] = scope.split("/");

  const manifest = window.__REMOTE_MANIFEST__;
  const remote = manifest?.[name];

  if (!remote) return;

  window.__REMOTE_REFRESH_TOKENS__ ??= {};
  window.__REMOTE_REFRESH_TOKENS__[name] =
    (window.__REMOTE_REFRESH_TOKENS__[name] ?? 0) + 1;

  const refreshToken = window.__REMOTE_REFRESH_TOKENS__[name];
  const cacheBustedEntry = `${remote.entry}${remote.entry.includes("?") ? "&" : "?"}v=${refreshToken}`;

  //   Keep manifest in sync
  window.__REMOTE_MANIFEST__ = {
    ...window.__REMOTE_MANIFEST__,
    [name]: {
      ...remote,
      entry: cacheBustedEntry,
    },
  };

  // Clear the old global container if it exists
  delete (window as any)[name];

  // Re-register the remote with the fresh URL
  registerRemotes([
    {
      name,
      alias: name,
      entry: cacheBustedEntry,
    },
  ]);

  console.info("[refreshRemote]", { name, cacheBustedEntry });
}
