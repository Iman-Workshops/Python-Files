"""آموزش تفاوت فایل متنی و فایل باینری.

خروجی مورد انتظار: ساخت یک فایل txt و یک فایل bin، سپس نمایش اندازه و بایت‌های فایل باینری.
"""

import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
TEXT_FILE = OUTPUT_DIR / "text_sample.txt"
BINARY_FILE = OUTPUT_DIR / "bytes_sample.bin"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)

    TEXT_FILE.write_text("فایل متنی با رشته کار می‌کند.\n", encoding="utf-8")

    # فایل باینری با bytes کار می‌کند، نه با str.
    data = bytes(range(16))
    BINARY_FILE.write_bytes(data)

    loaded_bytes = BINARY_FILE.read_bytes()

    print(f"فایل متنی: {TEXT_FILE}")
    print(f"اندازه فایل متنی: {TEXT_FILE.stat().st_size} بایت")
    print(f"فایل باینری: {BINARY_FILE}")
    print(f"اندازه فایل باینری: {BINARY_FILE.stat().st_size} بایت")
    print(f"بایت‌های خوانده شده: {list(loaded_bytes)}")


if __name__ == "__main__":
    main()
