import type { ComponentType } from "react";

const remoteFallbacks: Record<string, ComponentType<any>> = {
  "remote/Reviews": function ReviewsFallback() {
    return (
      <div style={{ padding: 16, border: "1px solid #ddd", borderRadius: 8 }}>
        <h3>Reviews temporarily unavailable</h3>
        <p>We could not load the Reviews remote right now.</p>
      </div>
    );
  },

  "cart/Cart": function CartFallback() {
    return (
      <div style={{ padding: 16, border: "1px solid #ddd", borderRadius: 8 }}>
        <h3>Cart temporarily unavailable 🏗️</h3>
        <p>We could not load the Cart remote right now.</p>
      </div>
    );
  },
};

export default remoteFallbacks;
