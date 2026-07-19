# Deployment

The included container serves the FastAPI application. The Kubernetes manifests are conservative examples and deliberately run one CPU replica. Configure a real checkpoint through a read-only volume or approved object store. The demo predictor is disabled in the Kubernetes example.

Before any external deployment, add authentication, TLS, request logging controls, image-retention policy, rate limits, vulnerability scanning, and a privacy review.
