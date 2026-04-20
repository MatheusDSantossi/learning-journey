import { Component, ErrorInfo, ReactNode, Suspense } from "react";

/**
 * This wrapper gives us a clean production pattern:

Suspense handles the loading state
ErrorBoundary handles the failure state

That separation matters because federated modules can fail in different ways:

network failure
wrong remote URL
bad exposed module name
runtime crash inside the remote
 */

type RemoteBoundaryProps = {
  title: string;
  loadingFallback?: ReactNode;
  children: ReactNode;
};

type RemoteBoundaryState = {
  hasError: boolean;
  error: Error | null;
};

class RemoteErrorBoundary extends Component<
  { title: string; children: ReactNode },
  RemoteBoundaryState
> {
  constructor(props: { title: string; children: ReactNode }) {
    super(props);
    this.state = {
      hasError: false,
      error: null,
    };
  }

  static getDerivedStateFromError(error: Error): RemoteBoundaryState {
    return {
      hasError: true,
      error,
    };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error(`[RemoteBoundary] ${this.props.title}`, error, errorInfo);
  }

  handleRetry = () => {
    this.setState({
      hasError: false,
      error: null,
    });
  };

  render() {
    if (this.state.hasError) {
      return (
        <div style={{ padding: 16, border: "1px solid #f99", borderRadius: 8 }}>
          <h2>{this.props.title} unavailable</h2>
          <p>Something went wrong while loading this remote.</p>
          <pre style={{ whiteSpace: "pre-wrap" }}>
            {this.state.error?.message}
          </pre>
          <button onClick={this.handleRetry}>Try again</button>
        </div>
      );
    }

    return this.props.children;
  }
}

export function RemoteBoundary({
  title,
  loadingFallback = <div>Loading remote...</div>,
  children,
}: RemoteBoundaryProps) {
  return (
    <RemoteErrorBoundary title={title}>
      <Suspense fallback={loadingFallback}>{children}</Suspense>
    </RemoteErrorBoundary>
  );
}
