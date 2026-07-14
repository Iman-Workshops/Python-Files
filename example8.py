"""آموزش جداکننده سفارشی و نقل‌قول در CSV.

خروجی مورد انتظار: ساخت courses_semicolon.csv با جداکننده ; و خواندن همان فایل.
"""

import csv
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
COURSES_FILE = OUTPUT_DIR / "courses_semicolon.csv"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)

    rows = [
        ["title", "teacher", "note"],
        ["Python Files", "مدرس کارگاه", "متن شامل، ویرگول"],
        ["CSV Basics", "مدرس کارگاه", 'متن شامل "کوتیشن"'],
    ]

    # delimiter جداکننده ستون‌ها را عوض می‌کند. quoting هنگام نیاز مقدار را داخل کوتیشن می‌گذارد.
    with COURSES_FILE.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";", quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)

    with COURSES_FILE.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file, delimiter=";")
        loaded_rows = list(reader)

    print(f"فایل CSV ساخته شد: {COURSES_FILE}")
    print("محتوای خام فایل:")
    print(COURSES_FILE.read_text(encoding="utf-8"))
    print("ردیف‌های خوانده شده:")
    for row in loaded_rows:
        print(row)


if __name__ == "__main__":
    main()
