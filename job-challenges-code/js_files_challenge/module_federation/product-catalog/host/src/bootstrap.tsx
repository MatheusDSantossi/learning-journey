import ReactDOM from "react-dom/client";
import {
  registerPlugins,
  registerRemotes,
} from "@module-federation/enhanced/runtime";
import App from "./App";
import { runtimeFallbackPlugin } from "./remotes/runtimeFallbackPlugin";
import { registerCartEventListeners } from "./events/cart.event";

type Manifest = Record<string, { entry: string; version: string }>;

declare global {
  interface Window {
    __REMOTE_MANIFEST__?: Manifest;
    __REMOTE_VERSIONS__?: Record<string, string>;
    __REMOTE_REFRESH_TOKENS__?: Record<string, number>;
  }
}

async function start() {
  const cleanupCartEvent = registerCartEventListeners();

  const response = await fetch("/manifest.json", { cache: "no-store" });

  if (!response.ok) {
    throw new Error(`Failed to load manifest.json (${response.status})`);
  }

  const manifest = (await response.json()) as Manifest;

  // Missing piece
  window.__REMOTE_MANIFEST__ = manifest;

  // !IMPORTANT Removed to test circuit break behavior
  // registerPlugins([runtimeFallbackPlugin()]);

  registerRemotes(
    Object.entries(manifest).map(([name, remote]) => ({
      name,
      alias: name,
      entry: remote.entry,
    })),
  );

  //   exposing it for debugging
  (window as any).__REMOTE_VERSIONS__ = Object.fromEntries(
    Object.entries(manifest).map(([name, remote]) => [name, remote.version]),
  );

  const root = ReactDOM.createRoot(
    document.getElementById("app") as HTMLElement,
  );
  root.render(<App />);

  return cleanupCartEvent;
}

void start().catch((error) => {
  console.error("[host bootstrap] failed to initialize remotes", error);
});
