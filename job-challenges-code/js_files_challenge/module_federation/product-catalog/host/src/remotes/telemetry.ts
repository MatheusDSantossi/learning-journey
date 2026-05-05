export type RemoteLoadStatus = "start" | "success" | "error";

export type RemoteTelemetryEvent = {
  remote: string;
  version: string;
  status: RemoteLoadStatus;
  at: string;
  durationMs?: number;
  error?: string;
};

declare global {
  interface Window {
    __REMOTE_VERSIONS__?: Record<string, string>;
    __REMOTE_TELEMETRY__?: RemoteTelemetryEvent[];
  }
}

function getRemoteVersion(remoteName: string) {
  return window.__REMOTE_VERSIONS__?.[remoteName] ?? "unkown";
}

function pushTelemetry(event: RemoteTelemetryEvent) {
  window.__REMOTE_TELEMETRY__ ??= [];
  window.__REMOTE_TELEMETRY__.push(event);

  const prefix = `[remote telemetry] ${event.remote}@${event.version}`;
  if (event.status === "error") {
    console.warn(prefix, event);
  } else {
    console.info(prefix, event);
  }
}

export async function withRemoteTelemetry<T>(
  scope: string,
  loader: () => Promise<T>,
): Promise<T> {
  const [remoteName] = scope.split("/");
  const version = getRemoteVersion(remoteName);
  const startedAt = performance.now();

  pushTelemetry({
    remote: remoteName,
    version,
    status: "start",
    at: new Date().toISOString(),
  });

  try {
    const result = await loader();

    pushTelemetry({
      remote: remoteName,
      version,
      status: "success",
      durationMs: performance.now() - startedAt,
      at: new Date().toISOString(),
    });

    return result;
  } catch (err) {
    pushTelemetry({
      remote: remoteName,
      version,
      status: "success",
      durationMs: performance.now() - startedAt,
      error: err instanceof Error ? err.message : String(err),
      at: new Date().toISOString(),
    });

    throw err;
  }
}
