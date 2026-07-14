"""حل نمونه تمرین‌های تکمیلی کار با فایل‌ها.

خروجی مورد انتظار: ساخت JSON امن، گزارش پوشه، فایل zip، پردازش CSV بزرگ و تنظیمات INI.
"""

import configparser
import csv
import json
import sys
import tempfile
import zipfile
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
ADVANCED_DIR = OUTPUT_DIR / "advanced_practice"
SAFE_JSON = ADVANCED_DIR / "settings_safe.json"
SAFE_BACKUP = ADVANCED_DIR / "settings_safe.backup.json"
TREE_DIR = ADVANCED_DIR / "tree"
TREE_REPORT = ADVANCED_DIR / "directory_report.json"
ZIP_SOURCE_DIR = ADVANCED_DIR / "zip_source"
ZIP_FILE = ADVANCED_DIR / "practice_archive.zip"
ZIP_EXTRACT_DIR = ADVANCED_DIR / "zip_extract"
BIG_CSV = ADVANCED_DIR / "big_orders.csv"
INI_FILE = ADVANCED_DIR / "app.ini"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def safe_write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        SAFE_BACKUP.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")

    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=path.parent,
        delete=False,
    ) as temp_file:
        json.dump(data, temp_file, ensure_ascii=False, indent=2)
        temp_path = Path(temp_file.name)

    temp_path.replace(path)


def solve_safe_json_task():
    safe_write_json(SAFE_JSON, {"version": 1, "autosave": True})
    safe_write_json(SAFE_JSON, {"version": 2, "autosave": False})
    print(f"فایل JSON امن ساخته شد: {SAFE_JSON}")


def solve_directory_report_task():
    files = {
        TREE_DIR / "notes" / "a.txt": "الف\n",
        TREE_DIR / "notes" / "b.txt": "ب\n",
        TREE_DIR / "data" / "scores.csv": "name,score\nSara,18\n",
    }

    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    records = []
    for path in sorted(TREE_DIR.rglob("*")):
        if path.is_file():
            records.append(
                {
                    "relative_path": str(path.relative_to(TREE_DIR)),
                    "size_bytes": path.stat().st_size,
                }
            )

    TREE_REPORT.write_text(
        json.dumps({"files": records}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"گزارش پوشه ساخته شد: {TREE_REPORT}")


def solve_zip_task():
    ZIP_SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    (ZIP_SOURCE_DIR / "readme.txt").write_text("نمونه zip\n", encoding="utf-8")
    (ZIP_SOURCE_DIR / "table.csv").write_text("name,score\nSara,18\n", encoding="utf-8")

    with zipfile.ZipFile(ZIP_FILE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(ZIP_SOURCE_DIR.iterdir()):
            archive.write(path, arcname=path.name)

    with zipfile.ZipFile(ZIP_FILE, "r") as archive:
        names = archive.namelist()
        archive.extractall(ZIP_EXTRACT_DIR)

    print(f"فایل zip ساخته شد: {ZIP_FILE}")
    print(f"تعداد فایل داخل zip: {len(names)}")


def iter_paid_orders(path):
    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["status"] == "paid":
                yield row


def solve_large_csv_task():
    with BIG_CSV.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["order_id", "amount", "status"])
        writer.writeheader()
        for number in range(1, 1001):
            writer.writerow(
                {
                    "order_id": number,
                    "amount": 5000 + number,
                    "status": "paid" if number % 4 else "canceled",
                }
            )

    count = 0
    total = 0
    for row in iter_paid_orders(BIG_CSV):
        count += 1
        total += int(row["amount"])

    print(f"تعداد سفارش پرداخت شده: {count}")
    print(f"جمع مبلغ: {total}")


def solve_ini_task():
    config = configparser.ConfigParser()
    config["app"] = {"language": "fa", "theme": "light", "autosave": "yes"}
    config["paths"] = {"output_dir": str(ADVANCED_DIR)}

    with INI_FILE.open("w", encoding="utf-8") as file:
        config.write(file)

    loaded = configparser.ConfigParser()
    loaded.read(INI_FILE, encoding="utf-8")
    loaded["app"]["theme"] = "dark"

    with INI_FILE.open("w", encoding="utf-8") as file:
        loaded.write(file)

    print(f"فایل تنظیمات ساخته شد: {INI_FILE}")


def main():
    configure_stdout()
    ADVANCED_DIR.mkdir(parents=True, exist_ok=True)
    solve_safe_json_task()
    solve_directory_report_task()
    solve_zip_task()
    solve_large_csv_task()
    solve_ini_task()


if __name__ == "__main__":
    main()
