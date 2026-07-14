"""آموزش read، readline، readlines و حلقه روی فایل.

خروجی مورد انتظار: ساخت فایل چندخطی و مقایسه روش‌های خواندن از نظر رفتار و حافظه.
"""

import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
LINES_FILE = OUTPUT_DIR / "many_lines.txt"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def make_sample_file():
    OUTPUT_DIR.mkdir(exist_ok=True)
    lines = [f"خط {number}: نمونه برای خواندن خط به خط\n" for number in range(1, 101)]
    LINES_FILE.write_text("".join(lines), encoding="utf-8")


def main():
    configure_stdout()
    make_sample_file()

    # read کل فایل را یکجا در حافظه می‌آورد.
    full_text = LINES_FILE.read_text(encoding="utf-8")

    # readline هر بار یک خط می‌خواند.
    with LINES_FILE.open("r", encoding="utf-8") as file:
        first_line = file.readline().strip()
        second_line = file.readline().strip()

    # readlines همه خط‌ها را در یک لیست قرار می‌دهد.
    with LINES_FILE.open("r", encoding="utf-8") as file:
        all_lines = file.readlines()

    # حلقه مستقیم روی فایل، خط‌ها را یکی یکی می‌خواند و برای فایل بزرگ مناسب‌تر است.
    line_count = 0
    with LINES_FILE.open("r", encoding="utf-8") as file:
        for _line in file:
            line_count += 1

    print(f"فایل ساخته شد: {LINES_FILE}")
    print(f"تعداد کاراکتر با read: {len(full_text)}")
    print(f"readline اول: {first_line}")
    print(f"readline دوم: {second_line}")
    print(f"تعداد خط با readlines: {len(all_lines)}")
    print(f"تعداد خط با حلقه روی فایل: {line_count}")


if __name__ == "__main__":
    main()
