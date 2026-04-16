import React, { lazy, Suspense, useState } from "react";

// Dynamically import the remote component
const RemoteReviews = lazy(() => import("remote/Reviews"));
const RemoteCart = lazy(() => import("cart/Cart"));

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
        <Suspense fallback={<div>Loading Reviews...</div>}>
          <RemoteReviews productId={selectedProduct} />
        </Suspense>
      )}

      <Suspense fallback={<div>Loading Cart...</div>}>
        <RemoteCart />
      </Suspense>
    </div>
  );
}

export default App;
