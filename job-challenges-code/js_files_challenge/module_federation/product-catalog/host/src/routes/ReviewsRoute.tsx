import { useParams } from "react-router-dom";
import { RemoteBoundary } from "../components/RemoteBoundary";
import { loadTypedRemote } from "../remotes/loadTypedRemote";

const RemoveReviews =
  loadTypedRemote<React.ComponentType<{ productId: string }>>("remote/Reviews");

export function ReviewsRoute() {
  const { productId } = useParams();

  if (!productId) {
    return <p>Missing product id.</p>;
  }

  return (
    <RemoteBoundary
      title="Reviews"
      loadingFallback={<div>Loading reviews...</div>}
    >
      <RemoveReviews productId={productId} />
    </RemoteBoundary>
  );
}

export default ReviewsRoute;
