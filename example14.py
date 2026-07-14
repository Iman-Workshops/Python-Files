"""آموزش نوشتن امن فایل با فایل موقت و جایگزینی اتمی.

خروجی مورد انتظار: ساخت inventory.json و backup با نسخه قبلی فایل.
"""

import json
import sys
import tempfile
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
TARGET_FILE = OUTPUT_DIR / "inventory.json"
BACKUP_FILE = OUTPUT_DIR / "inventory.backup.json"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def safe_write_json(path, data):
    path.parent.mkdir(exist_ok=True)

    if path.exists():
        BACKUP_FILE.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")

    # فایل موقت اول کامل نوشته می‌شود، سپس جای فایل اصلی را می‌گیرد.
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=path.parent,
        delete=False,
    ) as temp_file:
        json.dump(data, temp_file, ensure_ascii=False, indent=2)
        temp_path = Path(temp_file.name)

    temp_path.replace(path)


def main():
    configure_stdout()

    first_version = {"version": 1, "items": [{"name": "دفتر", "count": 12}]}
    second_version = {
        "version": 2,
        "items": [
            {"name": "دفتر", "count": 10},
            {"name": "خودکار", "count": 30},
        ],
    }

    safe_write_json(TARGET_FILE, first_version)
    safe_write_json(TARGET_FILE, second_version)

    print(f"فایل اصلی: {TARGET_FILE}")
    print(TARGET_FILE.read_text(encoding="utf-8"))
    print(f"نسخه پشتیبان وجود دارد؟ {BACKUP_FILE.exists()}")


if __name__ == "__main__":
    main()
