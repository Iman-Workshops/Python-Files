"""آموزش logging، سطح‌ها، قالب پیام و نوشتن در فایل.

خروجی مورد انتظار: ساخت app.log و نمایش پیام‌های DEBUG تا ERROR.
"""

import logging
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
LOG_FILE = OUTPUT_DIR / "app.log"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def build_logger():
    logger = logging.getLogger("workshop_example9")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()
    logger.propagate = False

    handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(handler)
    return logger


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)

    logger = build_logger()
    logger.debug("جزئیات عیب‌یابی ثبت شد")
    logger.info("برنامه اجرا شد")
    logger.warning("یک هشدار آموزشی ثبت شد")
    logger.error("یک خطای آموزشی ثبت شد")

    print(f"فایل لاگ ساخته شد: {LOG_FILE}")
    print(LOG_FILE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
