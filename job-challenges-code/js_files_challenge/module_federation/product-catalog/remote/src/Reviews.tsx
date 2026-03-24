import React, { useState } from "react";

interface Review {
  id: number;
  text: string;
  rating: number;
}

interface ReviewsProps {
  productId: string;
}

const Reviews: React.FC<ReviewsProps> = ({ productId }) => {
  const [reviews, setReviews] = useState<Review[]>([
    { id: 1, text: "Great product!", rating: 5 },
    { id: 2, text: "Good value", rating: 4 },
  ]);

  const addReview = () => {
    const newReview = {
      id: reviews.length + 1,
      text: `New review for product ${productId}`,
      rating: 3,
    };
    setReviews([...reviews, newReview]);
  };

  return (
    <div style={{ border: "1px solid #ccc", padding: "1rem" }}>
      <h3>Reviews for product {productId}</h3>
      <ul>
        {reviews.map((review) => (
          <li key={review.id}>
            {review.text} (Rating: {review.rating})
          </li>
        ))}
      </ul>
      <button onClick={addReview}>Add Sample Review</button>
    </div>
  );
};

export default Reviews;
