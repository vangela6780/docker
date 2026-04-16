import argparse
import logging
import os
import sys
from datetime import datetime
from pathlib import Path

import qrcode
import validators
from dotenv import load_dotenv

# Load optional environment variables from .env when present.
load_dotenv()

QR_DIRECTORY = os.getenv("QR_CODE_DIR", "qr_codes")
FILL_COLOR = os.getenv("FILL_COLOR", "red")
BACK_COLOR = os.getenv("BACK_COLOR", "white")


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


def create_directory(path: Path) -> None:
    try:
        path.mkdir(parents=True, exist_ok=True)
    except Exception as error:
        logging.error("Failed to create directory %s: %s", path, error)
        raise SystemExit(1) from error


def is_valid_url(url: str) -> bool:
    if validators.url(url):
        return True

    logging.error("Invalid URL provided: %s", url)
    return False


def generate_qr_code(data: str, path: Path, fill_color: str = "red", back_color: str = "white") -> None:
    if not is_valid_url(data):
        raise SystemExit(1)

    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        image = qr.make_image(fill_color=fill_color, back_color=back_color)

        with path.open("wb") as qr_file:
            image.save(qr_file)

        logging.info("QR code successfully saved to %s", path)
    except Exception as error:
        logging.error("An error occurred while generating or saving the QR code: %s", error)
        raise SystemExit(1) from error


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a QR code.")
    parser.add_argument("--url", default="https://github.com/kaw393939", help="The URL to encode in the QR code")
    args = parser.parse_args()

    setup_logging()

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    qr_filename = f"QRCode_{timestamp}.png"

    output_dir = Path.cwd() / QR_DIRECTORY
    qr_code_full_path = output_dir / qr_filename

    create_directory(output_dir)
    generate_qr_code(args.url, qr_code_full_path, FILL_COLOR, BACK_COLOR)


if __name__ == "__main__":
    main()
