import React from "react";
import { Link, NavLink, Outlet } from "react-router-dom";
import { prefetchRemote } from "../remotes/prefetchRemote";

const ShellLayout = () => {
  return (
    <div style={{ minHeight: "100vh", background: "#f7f7f8" }}>
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
            <NavLink
              to="/"
              onMouseEnter={() => prefetchRemote("cart/Cart")}
              onFocus={() => prefetchRemote("cart/Cart")}
            >
              Home
            </NavLink>
            <NavLink to="/cart">Cart</NavLink>
          </nav>
        </div>
      </header>

      <main style={{ maxWidth: 1100, margin: "0 auto", padding: 24 }}>
        <Outlet />
      </main>
    </div>
  );
};

export default ShellLayout;
