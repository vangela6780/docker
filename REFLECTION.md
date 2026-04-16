# Reflection

## What I built
I created a Dockerized QR code generator application and validated that it runs successfully in a containerized environment. 

## The Docker Hub link for my image
https://hub.docker.com/r/angelavazquez/qr-code-generator-app

## What worked well
- The container built and ran as expected.
- Volume mounting worked correctly, and the generated QR code file was saved to the host machine.
- Logs clearly confirmed successful execution and output file creation.

## Challenges and how I solved them
- Understanding host-to-container path mapping for volume mounts required careful testing.
- I verified the mapping by checking for generated files in the host output directory after the container exited.

## CI/CD automation
I added a GitHub Actions workflow that builds the Docker image on pushes and pull requests to `main` as a smoke test.

## What I learned
- How to package an app with Docker and run it consistently.
- How Docker volume mounts enable data persistence between container and host.
- How to automate container build validation with GitHub Actions.

## Next improvements
- Add automated runtime tests in CI (not just build).
- Add image tagging by commit SHA/version.
- Add vulnerability scanning for the Docker image.
