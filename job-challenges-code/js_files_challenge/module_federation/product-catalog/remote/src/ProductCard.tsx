type ProductCardProps = {
  productId: string;
  title: string;
  price: number;
  quantity: number;
};

export function ProductCard({
  productId,
  title,
  price,
  quantity,
}: ProductCardProps) {
  const handleAddToCart = () => {
    console.log("entered here!");
    window.dispatchEvent(
      new CustomEvent("cart:add", {
        detail: {
          productId,
          title,
          price,
          quantity,
        },
      }),
    );
  };

  return (
    <div>
      <h3>{title}</h3>
      <p>${price}</p>
      <button onClick={handleAddToCart}>Add to Cart</button>
    </div>
  );
}
