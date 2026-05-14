import { useMemo } from "react";
import { RemoteBoundary } from "../components/RemoteBoundary";
import { useRemoteRetry } from "../hooks/useRemoteRetry";
import { loadTypedRemote } from "../remotes/loadTypedRemote";

// const RemoteCart = loadTypedRemote<React.ComponentType<{}>>("cart/Cart");

export function CartRoute() {
  const retryToken = useRemoteRetry("cart/Cart");

  const RemoteCart = useMemo(
    () => loadTypedRemote<React.ComponentType>("cart/Cart"),
    [retryToken],
  );

  return (
    <RemoteBoundary
      key={retryToken}
      title="Cart"
      loadingFallback={<div>Loading cart...</div>}
      // resetKeys={[String(retryToken)]}
    >
      <RemoteCart />
    </RemoteBoundary>
  );
}
