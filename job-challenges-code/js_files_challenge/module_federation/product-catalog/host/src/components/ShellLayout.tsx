import React from "react";
import { Link, NavLink, Outlet } from "react-router-dom";
import { prefetchRemote } from "../remotes/prefetchRemote";
import Navbar from "./Navbar";

const ShellLayout = () => {
  return (
    <div style={{ minHeight: "100vh", background: "#f7f7f8" }}>
      <Navbar />

      <main style={{ maxWidth: 1100, margin: "0 auto", padding: 24 }}>
        <Outlet />
      </main>
    </div>
  );
};

export default ShellLayout;
