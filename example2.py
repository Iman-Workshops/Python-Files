"""آموزش کدگذاری UTF-8، BOM و خطای decode برای متن فارسی.

خروجی مورد انتظار: ساخت چند فایل متنی و نمایش تفاوت خواندن درست و خواندن اشتباه.
"""

import locale
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
UTF8_FILE = OUTPUT_DIR / "persian_utf8.txt"
BOM_FILE = OUTPUT_DIR / "persian_with_bom.txt"
BROKEN_FILE = OUTPUT_DIR / "broken_bytes.txt"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)

    text = "سلام، این متن فارسی با UTF-8 ذخیره شده است.\n"
    UTF8_FILE.write_text(text, encoding="utf-8")

    # utf-8-sig در ابتدای فایل یک BOM می‌نویسد. بعضی برنامه‌ها از آن برای تشخیص UTF-8 کمک می‌گیرند.
    BOM_FILE.write_text(text, encoding="utf-8-sig")

    # این فایل عمدا بایت‌های نامعتبر برای UTF-8 دارد تا خطای decode دیده شود.
    BROKEN_FILE.write_bytes(b"\xff\xfe\x00P\x00y\x00")

    default_encoding = locale.getpreferredencoding(False)
    bom_start = list(BOM_FILE.read_bytes()[:3])

    print(f"کدگذاری پیش‌فرض این سیستم: {default_encoding}")
    print(f"خواندن درست UTF-8: {UTF8_FILE.read_text(encoding='utf-8').strip()}")
    print(f"سه بایت اول فایل دارای BOM: {bom_start}")
    print(f"خواندن فایل دارای BOM با utf-8-sig: {BOM_FILE.read_text(encoding='utf-8-sig').strip()}")

    try:
        BROKEN_FILE.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        print("خواندن فایل خراب با UTF-8 خطا داد.")
        print(f"نوع خطا: {type(error).__name__}")


if __name__ == "__main__":
    main()
