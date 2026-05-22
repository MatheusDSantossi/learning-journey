type CartItem = {
  productId: string;
  title: string;
  price: number;
  quantity: number;
};

type CartState = {
  items: CartItem[];
};

const state: CartState = {
  items: [],
};

const listeners = new Set<() => void>();

function emitChange() {
  listeners.forEach((listener) => listener());
}

export function getCartState() {
  return state;
}

export function subscribeToCart(listener: () => void) {
  listeners.add(listener);
  return () => listeners.delete(listener);
}

export function addToCart(item: CartItem) {
  const existing = state.items.find((x) => x.productId === item.productId);

  if (existing) {
    existing.quantity += item.quantity;
  } else {
    state.items.push(item);
  }

  emitChange();
}
