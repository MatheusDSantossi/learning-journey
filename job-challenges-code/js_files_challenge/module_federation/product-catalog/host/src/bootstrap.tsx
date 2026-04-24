import ReactDOM from "react-dom/client";
import { registerRemotes } from "@module-federation/enhanced/runtime";
import App from "./App";

type Manifest = Record<string, { entry: string; version: string }>;

async function start() {
  const response = await fetch("/manifest.json", { cache: "no-store" });

  if (!response.ok) {
    throw new Error(`Failed to load manifest.json (${response.status})`);
  }

  const manifest = (await response.json()) as Manifest;

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
}

void start().catch((error) => {
  console.error("[host bootstrap] failed to initialize remotes", error);
});
