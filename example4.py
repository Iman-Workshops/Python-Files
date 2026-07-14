"""آموزش context manager و بستن فایل.

خروجی مورد انتظار: نمایش بسته شدن خودکار فایل با with و بستن دستی فایل در finally.
"""

import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
CONTEXT_FILE = OUTPUT_DIR / "context_manager.txt"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def write_with_context_manager():
    with CONTEXT_FILE.open("w", encoding="utf-8") as file:
        file.write("این خط داخل بلوک with نوشته شد.\n")
        inside_status = file.closed

    return inside_status, file.closed


def write_with_try_finally():
    file = CONTEXT_FILE.open("a", encoding="utf-8")
    try:
        file.write("این خط با try/finally نوشته شد.\n")
        return file.closed
    finally:
        file.close()


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)

    inside_with, after_with = write_with_context_manager()
    before_finally_close = write_with_try_finally()

    print(f"فایل ساخته شد: {CONTEXT_FILE}")
    print(f"داخل with فایل بسته بود؟ {inside_with}")
    print(f"بعد از with فایل بسته بود؟ {after_with}")
    print(f"قبل از finally فایل بسته بود؟ {before_finally_close}")
    print(CONTEXT_FILE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
