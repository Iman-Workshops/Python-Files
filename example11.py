"""آموزش مدیریت خطاهای فایل با try، except و finally.

خروجی مورد انتظار: نمایش پیام FileNotFoundError و سپس خواندن موفق یک فایل واقعی.
"""

import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
REAL_FILE = OUTPUT_DIR / "safe_read.txt"
MISSING_FILE = OUTPUT_DIR / "missing.txt"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def read_text_file(path):
    try:
        file = path.open("r", encoding="utf-8")
        try:
            return file.read()
        finally:
            file.close()
            print(f"فایل بسته شد: {path.name}")
    except FileNotFoundError:
        print(f"فایل پیدا نشد: {path}")
    except PermissionError:
        print(f"اجازه خواندن فایل وجود ندارد: {path}")

    return ""


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)
    REAL_FILE.write_text("این فایل برای خواندن امن ساخته شد.\n", encoding="utf-8")

    read_text_file(MISSING_FILE)
    content = read_text_file(REAL_FILE)

    print("محتوای فایل واقعی:")
    print(content)


if __name__ == "__main__":
    main()
