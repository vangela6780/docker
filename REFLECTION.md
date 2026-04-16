# Reflection

## What I built
I Dockerized a Python QR code generator application, ran it in a container, and verified that QR output files are written to a mounted host directory.

## Environment setup
- Installed Docker Desktop with WSL2 backend on Windows.
- Installed Ubuntu in WSL2 for Linux-based Docker development and command-line workflow.
- Verified Docker installation with `docker --version`.

## The Docker Hub link for my image
https://hub.docker.com/r/angelavazquez/qr-code-generator-app

## What worked well
- A secure non-root Docker image was built successfully from the project Dockerfile.
- Volume mounting worked correctly, and generated QR code files were saved to the host output folder.
- Container logs confirmed successful QR generation.

## Challenges and how I solved them
- Understanding host-to-container path mapping for volume mounts required careful testing.
- I verified the mapping by checking for generated files in the host output directory after the container exited.

## CI/CD automation
I added a GitHub Actions workflow that:
- Builds the Docker image on push and pull request to `main`.
- Runs the container with a test URL.
- Verifies at least one QR code artifact is generated in the mounted output directory.

## What I learned
- How to package an app with Docker and run it consistently.
- How Docker volume mounts enable data persistence between container and host.
- How to automate both container build and runtime validation with GitHub Actions.

## Next improvements
- Add image tagging by commit SHA/version.
- Add vulnerability scanning for the Docker image.
