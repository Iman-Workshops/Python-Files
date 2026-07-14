"""آموزش pathlib برای مسیرهای قابل اجرا در سیستم‌عامل‌های مختلف.

خروجی مورد انتظار: ساخت چند فایل در پوشه داده و پیدا کردن آن‌ها با glob.
"""

import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
DATA_DIR = OUTPUT_DIR / "pathlib_demo" / "data"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def main():
    configure_stdout()
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    notes = {
        "lesson1.txt": "مسیرها با pathlib ساخته شدند.\n",
        "lesson2.txt": "این فایل برای تمرین glob است.\n",
        "readme.md": "# فایل نمونه\n",
    }

    for name, content in notes.items():
        (DATA_DIR / name).write_text(content, encoding="utf-8")

    text_files = sorted(DATA_DIR.glob("*.txt"))

    print(f"پوشه پایه مخزن: {BASE_DIR}")
    print(f"پوشه خروجی وجود دارد؟ {OUTPUT_DIR.exists()}")
    print(f"پوشه داده ساخته شد: {DATA_DIR}")
    print("فایل‌های txt پیدا شده با glob:")
    for path in text_files:
        print(f"- {path.name}: {path.read_text(encoding='utf-8').strip()}")


if __name__ == "__main__":
    main()
