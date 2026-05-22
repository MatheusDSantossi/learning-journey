import React from "react";
import { ProductCard } from "../../remote/src/ProductCard";

const remoteVersions = (window as any).__REMOTE_VERSIONS__ as
  | Record<string, string>
  | undefined;

export default function Cart() {
  return (
    <div>
      <h2>🛒 Cart Micro-Frontend</h2>
      <p>This is coming from another remote (remote-cart)</p>
      <ProductCard productId="123" title="Keybord" price={99} quantity={1} />
      <small>v{remoteVersions?.cart ?? "unknown"}</small>
    </div>
  );
}
