import { Link, NavLink } from "react-router-dom";
import { prefetchRemote } from "../remotes/prefetchRemote";
import { useCart } from "../../../remote-cart/src/hooks/useCart";

const Navbar = () => {
  const cart = useCart();
  const count = cart.items.reduce((sum, item) => sum + item.quantity, 0);

  return (
    <>
      <header style={{ borderBottom: "1px solid #ddd", background: "#fff" }}>
        <div
          style={{
            maxWidth: 1100,
            margin: "0 auto",
            padding: "16px 24px",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          }}
        >
          <Link to="/" style={{ fontWeight: 700, textDecoration: "none" }}>
            Product Catalog
          </Link>

          <nav style={{ display: "flex", gap: 16 }}>
            <NavLink to="/">Home</NavLink>
            <NavLink
              to="/cart"
              onMouseEnter={() => prefetchRemote("cart/Cart")}
              onFocus={() => prefetchRemote("cart/Cart")}
            >
              Cart {count}
            </NavLink>
          </nav>
        </div>
      </header>
    </>
  );
};

export default Navbar;
