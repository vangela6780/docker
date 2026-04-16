# Rubric Checklist and Evidence

## 1. Submission Completeness (50 points)

### GitHub Repository Link (15)
- Repository: https://github.com/vangela6780/docker
- Includes required files:
  - `Dockerfile`
  - `main.py`
  - `requirements.txt`
  - `.github/workflows/main.yml`
  - `REFLECTION.md`

### DockerHub Image Link (15)
- Image repository: https://hub.docker.com/r/angelavazquez/qr-code-generator-app
- Example pull command:
  - `docker pull angelavazquez/qr-code-generator-app:latest`

### Screenshots (10)
- Container logs screenshot: `command.png`
- GitHub Actions successful run screenshot: `githubActions.png`

### Reflection Document (10)
- Reflection file: `REFLECTION.md`

## 2. Functionality of Dockerized Application (50 points)

### Docker Image Builds Successfully (25)
- Docker build command:
  - `docker build -t qr-code-generator-app .`
- CI workflow also builds image on push and PR.

### Container Runs Correctly (25)
- Docker run command:
  - `docker run --rm -v ${PWD}/qr_output:/app/qr_codes qr-code-generator-app --url https://www.njit.edu`
- Expected behavior:
  - Logs show successful QR generation.
  - PNG file appears in `qr_output`.
- CI runtime validation:
  - Runs container.
  - Verifies generated PNG exists.
  - Uploads generated PNG as artifact (`qr-output`).

## Environment Setup Evidence
- WSL2/Ubuntu check output (Windows):
  - `wsl -l -v` returns `Ubuntu` with `VERSION 2`.

## Final Submission Package
- GitHub link
- DockerHub link
- `command.png`
- `githubActions.png`
- `REFLECTION.md`
