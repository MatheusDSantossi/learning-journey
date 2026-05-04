import { RemoteBoundary } from "../components/RemoteBoundary";
import { loadTypedRemote } from "../remotes/loadTypedRemote";

const RemoteCart = loadTypedRemote<React.ComponentType<{}>>("cart/Cart");

export function CartRoute() {
  return (
    <RemoteBoundary title="Cart" loadingFallback={<div>Loading cart...</div>}>
      <RemoteCart />
    </RemoteBoundary>
  );
}
