"""آموزش حالت‌های r، w، a و r+ برای فایل متنی.

خروجی مورد انتظار: ساخت فایل modes.txt، اضافه شدن چند خط، و نمایش محتوای نهایی.
"""

import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
TEXT_FILE = OUTPUT_DIR / "modes.txt"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)

    # حالت w فایل را می‌سازد. اگر فایل قبلی وجود داشته باشد، محتوای آن پاک می‌شود.
    with TEXT_FILE.open("w", encoding="utf-8") as file:
        file.write("خط 1: این فایل با حالت w ساخته شد.\n")
        file.write("خط 2: متن فارسی با UTF-8 ذخیره شد.\n")

    # حالت a داده تازه را به انتهای فایل اضافه می‌کند.
    with TEXT_FILE.open("a", encoding="utf-8") as file:
        file.write("خط 3: این خط با حالت a اضافه شد.\n")

    # حالت r فقط برای خواندن است و فایل باید از قبل وجود داشته باشد.
    with TEXT_FILE.open("r", encoding="utf-8") as file:
        before_r_plus = file.read()

    # حالت r+ برای خواندن و نوشتن روی فایل موجود است. نشانگر فایل مهم است.
    with TEXT_FILE.open("r+", encoding="utf-8") as file:
        first_line = file.readline().strip()
        file.seek(0, 2)
        file.write("خط 4: این خط با حالت r+ و seek به انتهای فایل رفت.\n")

    final_content = TEXT_FILE.read_text(encoding="utf-8")

    print(f"فایل ساخته شد: {TEXT_FILE}")
    print(f"اولین خط خوانده شده با r+: {first_line}")
    print("محتوا قبل از r+:")
    print(before_r_plus)
    print("محتوای نهایی:")
    print(final_content)


if __name__ == "__main__":
    main()
