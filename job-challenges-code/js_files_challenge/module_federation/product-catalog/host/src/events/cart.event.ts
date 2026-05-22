import { addToCart } from "../stores/cart.store";

type CartAddEvent = CustomEvent<{
  productId: string;
  title: string;
  price: number;
  quantity?: number;
}>;

export function registerCartEventListeners() {
  const onAddToCart = (event: Event) => {
    const customEvent = event as CartAddEvent;
    const { productId, title, price, quantity = 1 } = customEvent.detail;

    addToCart({
      productId,
      title,
      price,
      quantity,
    });
  };

  window.addEventListener("cart:add", onAddToCart);

  return () => {
    window.removeEventListener("cart:add", onAddToCart);
  };
}
