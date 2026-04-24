import { lazy, Suspense, useState } from "react";
import { RemoteBoundary } from "./components/RemoteBoundary";
import { loadRemote } from "@module-federation/enhanced/runtime";
import { loadTypedRemote } from "./utils/utilFunctions";

// Dynamically import the remote component
// const RemoteReviews = lazy(() => import("remote/Reviews"));
// const RemoteCart = lazy(() => import("cart/Cart"));

// Dynamically load remotes from the runtime registry
const RemoteReviews =
  loadTypedRemote<React.ComponentType<{ productId: string }>>("remote/Reviews");

const RemoteCart = loadTypedRemote<React.ComponentType<{}>>("cart/Cart");

// lazy(() =>
//   loadRemote("cart/Cart").then((mod: any) => ({
//     default: mod.default ?? mod,
//   })),
// );

const products = [
  { id: "1", name: "Laptop" },
  { id: "2", name: "Mouse" },
  { id: "3", name: "Keyboard" },
];

function App() {
  const [selectedProduct, setSelectedProduct] = useState<string | null>(null);

  return (
    <div>
      <h1>Product Catalog</h1>

      <section style={{ marginBottom: 24 }}>
        <h2>Cart</h2>
        <RemoteBoundary
          title="Cart"
          loadingFallback={<div>Loading cart...</div>}
        >
          <RemoteCart />
        </RemoteBoundary>
      </section>

      <section>
        <ul>
          {products.map((product) => (
            <li key={product.id}>
              {product.name}{" "}
              <button onClick={() => setSelectedProduct(product.id)}>
                Show Reviews
              </button>
            </li>
          ))}
        </ul>

        {selectedProduct && (
          <RemoteBoundary
            title="Reviews"
            loadingFallback={<div>Loading reviews...</div>}
          >
            <RemoteReviews productId={selectedProduct} />
          </RemoteBoundary>
        )}
      </section>
    </div>
  );
}

export default App;
