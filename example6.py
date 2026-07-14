"""آموزش JSON با داده تو در تو و خطای JSON خراب.

خروجی مورد انتظار: ساخت profile.json، خواندن آن، و نمایش خطای فایل JSON نامعتبر.
"""

import json
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
PROFILE_FILE = OUTPUT_DIR / "profile.json"
BROKEN_JSON_FILE = OUTPUT_DIR / "broken_profile.json"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)

    profile = {
        "name": "سارا",
        "city": "کرمان",
        "skills": ["Python", "JSON", "فایل"],
        "scores": {"files": 18.5, "csv": 17.25},
        "active": True,
    }

    with PROFILE_FILE.open("w", encoding="utf-8") as file:
        json.dump(profile, file, ensure_ascii=False, indent=2)

    with PROFILE_FILE.open("r", encoding="utf-8") as file:
        loaded_profile = json.load(file)

    BROKEN_JSON_FILE.write_text('{"name": "سارا", "city": "کرمان",}', encoding="utf-8")

    print(f"فایل JSON ساخته شد: {PROFILE_FILE}")
    print(f"نام خوانده شده: {loaded_profile['name']}")
    print(f"مهارت دوم: {loaded_profile['skills'][1]}")

    try:
        json.loads(BROKEN_JSON_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        print("فایل JSON خراب خوانده نشد.")
        print(f"خطا در خط {error.lineno} و ستون {error.colno}")


if __name__ == "__main__":
    main()
