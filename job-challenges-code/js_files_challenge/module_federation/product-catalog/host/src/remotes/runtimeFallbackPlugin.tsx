import React from "react";
import type { ModuleFederationRuntimePlugin } from "@module-federation/enhanced/runtime";

function ReviewsFallback() {
  return (
    <div style={{ padding: 16, border: "1px solid #ddd", borderRadius: 8 }}>
      <h3>Reviews temporarily unavailable</h3>
      <p>We could not load the Reviews remote right now.</p>
    </div>
  );
}

function CartFallback() {
  return (
    <div style={{ padding: 16, border: "1px solid #ddd", borderRadius: 8 }}>
      <h3>Cart temporarily unavailable</h3>
      <p>We could not load the Cart remote right now.</p>
    </div>
  );
}

export function runtimeFallbackPlugin(): ModuleFederationRuntimePlugin {
  return {
    name: "runtime-fallback-plugin",
    async errorLoadRemote(args) {
      if (args.id === "remote/Reviews") {
        return { default: ReviewsFallback };
      }
      if (args.id === "cart/Cart") {
        return { default: CartFallback };
      }

      //   Let other remotes continue to the normal error boundary
      return undefined;
    },
  };
}
