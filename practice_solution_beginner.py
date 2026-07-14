"""حل نمونه تمرین‌های مقدماتی کار با فایل‌ها.

خروجی مورد انتظار: ساخت فایل متنی، فایل دارای BOM و چند فایل پیدا شده با glob.
"""

import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
NOTES_FILE = OUTPUT_DIR / "daily_notes.txt"
BOM_FILE = OUTPUT_DIR / "beginner_bom.txt"
PATH_DIR = OUTPUT_DIR / "path_practice" / "data"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def solve_text_file_task():
    OUTPUT_DIR.mkdir(exist_ok=True)

    with NOTES_FILE.open("w", encoding="utf-8") as file:
        file.write("خط اول تمرین متنی\n")
        file.write("خط دوم تمرین متنی\n")
        file.write("خط سوم تمرین متنی\n")

    with NOTES_FILE.open("a", encoding="utf-8") as file:
        file.write("خط چهارم با حالت a اضافه شد\n")

    print("محتوای فایل متنی:")
    for number, line in enumerate(NOTES_FILE.read_text(encoding="utf-8").splitlines(), start=1):
        print(f"{number}: {line}")


def solve_line_reading_task():
    with NOTES_FILE.open("r", encoding="utf-8") as file:
        first_line = file.readline().strip()

    with NOTES_FILE.open("r", encoding="utf-8") as file:
        lines_with_readlines = file.readlines()

    loop_count = 0
    with NOTES_FILE.open("r", encoding="utf-8") as file:
        for _line in file:
            loop_count += 1

    print(f"خط اول: {first_line}")
    print(f"تعداد خط با readlines: {len(lines_with_readlines)}")
    print(f"تعداد خط با حلقه: {loop_count}")


def solve_encoding_task():
    BOM_FILE.write_text("متن فارسی با BOM\n", encoding="utf-8-sig")
    first_bytes = list(BOM_FILE.read_bytes()[:3])
    print(f"سه بایت اول فایل دارای BOM: {first_bytes}")


def solve_path_task():
    PATH_DIR.mkdir(parents=True, exist_ok=True)

    for number in range(1, 4):
        path = PATH_DIR / f"note_{number}.txt"
        path.write_text(f"فایل شماره {number}\n", encoding="utf-8")

    print("فایل‌های پیدا شده با glob:")
    for path in sorted(PATH_DIR.glob("*.txt")):
        print(path.name)


def main():
    configure_stdout()
    solve_text_file_task()
    solve_line_reading_task()
    solve_encoding_task()
    solve_path_task()


if __name__ == "__main__":
    main()
