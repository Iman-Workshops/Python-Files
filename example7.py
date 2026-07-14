"""آموزش CSV با سرستون، DictWriter و DictReader.

خروجی مورد انتظار: ساخت people.csv و چاپ ردیف‌ها با نام ستون‌ها.
"""

import csv
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
PEOPLE_FILE = OUTPUT_DIR / "people.csv"
FIELDNAMES = ["name", "age", "city"]


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)

    people = [
        {"name": "سارا", "age": 22, "city": "کرمان"},
        {"name": "رضا", "age": 28, "city": "یزد"},
        {"name": "مریم", "age": 31, "city": "شیراز"},
    ]

    with PEOPLE_FILE.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(people)

    with PEOPLE_FILE.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        loaded_people = list(reader)

    print(f"فایل CSV ساخته شد: {PEOPLE_FILE}")
    for person in loaded_people:
        print(f"{person['name']}، {person['age']} ساله، شهر {person['city']}")


if __name__ == "__main__":
    main()
