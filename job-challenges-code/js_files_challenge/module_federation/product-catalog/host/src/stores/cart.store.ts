type CartItem = {
  productId: string;
  title: string;
  price: number;
  quantity: number;
};

type CartState = {
  items: CartItem[];
};

let state: CartState = {
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
    state = {
      ...state,
      items: state.items.map((x) =>
        x.productId === item.productId
          ? { ...x, quantity: x.quantity + item.quantity }
          : x,
      ),
    };
    // existing.quantity += item.quantity;
  } else {
    state = {
      ...state,
      items: [...state.items, item],
    };
    // state.items.push(item);
  }

  emitChange();
}
