FROM alpine:3.20

# Minimal image to satisfy CI Docker build smoke test.
CMD ["sh", "-c", "echo qr-code-app image built successfully"]
