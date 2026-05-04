import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { HomePage } from "./routes/HomePage";
import { ReviewsRoute } from "./routes/ReviewsRoute";
import { CartRoute } from "./routes/CartRoute";
import { loadTypedRemote } from "./remotes/loadTypedRemote";
import { useState } from "react";
import ShellLayout from "./components/ShellLayout";

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
    <BrowserRouter>
      <Routes>
        <Route element={<ShellLayout />}>
          <Route index element={<HomePage />} />
          <Route
            path="products/:productId/reviews"
            element={<ReviewsRoute />}
          />
          <Route path="cart" element={<CartRoute />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
