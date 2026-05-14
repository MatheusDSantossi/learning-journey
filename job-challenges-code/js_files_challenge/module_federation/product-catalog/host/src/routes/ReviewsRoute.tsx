import { useParams } from "react-router-dom";
import { RemoteBoundary } from "../components/RemoteBoundary";
import { loadTypedRemote } from "../remotes/loadTypedRemote";
import { useRemoteRetry } from "../hooks/useRemoteRetry";
import { useMemo } from "react";

// const RemoveReviews =
//   loadTypedRemote<React.ComponentType<{ productId: string }>>("remote/Reviews");

export function ReviewsRoute() {
  const { productId } = useParams();
  const retryToken = useRemoteRetry("remote/Reviews");

  const RemoveReviews = useMemo(
    () =>
      loadTypedRemote<React.ComponentType<{ productId: string }>>(
        "remote/Reviews",
      ),
    [retryToken],
  );

  if (!productId) {
    return <p>Missing product id.</p>;
  }

  return (
    <RemoteBoundary
      key={retryToken}
      title="Reviews"
      loadingFallback={<div>Loading reviews...</div>}
      // resetKeys={[String(retryToken)]}
    >
      <RemoveReviews productId={productId} />
    </RemoteBoundary>
  );
}

export default ReviewsRoute;
