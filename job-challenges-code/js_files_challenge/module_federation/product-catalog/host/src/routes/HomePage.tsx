import { Link } from "react-router-dom";

const products = [
  { id: "1", name: "Laptop" },
  { id: "2", name: "Mouse" },
  { id: "3", name: "Keyboard" },
];

export function HomePage() {
  return (
    <div>
      <h1>Products</h1>

      <ul style={{ listStyle: "none", padding: 0 }}>
        {products.map((product) => (
          <li
            key={product.id}
            style={{
              padding: "12px 0",
              borderBottom: "1px solid #e5e5e5",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <span>{product.name}</span>

            <div style={{ display: "flex", gap: 12 }}>
              <Link to={`/products/${product.id}/reviews`}>View reviews</Link>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
