"""حل نمونه تمرین‌های میانی JSON، CSV و گزارش‌گیری.

خروجی مورد انتظار: ساخت settings.json، مدیریت JSON خراب، و ساخت orders_report.json.
"""

import csv
import json
import logging
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
SETTINGS_FILE = OUTPUT_DIR / "settings.json"
BROKEN_JSON_FILE = OUTPUT_DIR / "settings_broken.json"
STUDENTS_FILE = OUTPUT_DIR / "practice_students_mid.csv"
COURSES_FILE = OUTPUT_DIR / "practice_courses_semicolon.csv"
ORDERS_FILE = OUTPUT_DIR / "practice_orders.csv"
REPORT_FILE = OUTPUT_DIR / "orders_report.json"
LOG_FILE = OUTPUT_DIR / "practice.log"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def solve_json_tasks():
    settings = {
        "language": "fa",
        "theme": "light",
        "font_size": 16,
        "autosave": True,
        "recent_files": ["notes.txt", "students.csv"],
    }

    SETTINGS_FILE.write_text(
        json.dumps(settings, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    loaded_settings = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    loaded_settings["autosave"] = False
    SETTINGS_FILE.write_text(
        json.dumps(loaded_settings, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    BROKEN_JSON_FILE.write_text('{"autosave": true,}', encoding="utf-8")
    try:
        json.loads(BROKEN_JSON_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        print(f"JSON خراب در خط {error.lineno} خوانده نشد.")


def solve_students_csv_task():
    rows = [
        {"name": "سارا", "score": "18", "passed": "yes"},
        {"name": "رضا", "score": "15.5", "passed": "yes"},
        {"name": "مریم", "score": "bad", "passed": "yes"},
        {"name": "نگار", "score": "9", "passed": "no"},
    ]

    with STUDENTS_FILE.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "score", "passed"])
        writer.writeheader()
        writer.writerows(rows)

    print("دانشجوهای قبول شده:")
    with STUDENTS_FILE.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for line_number, row in enumerate(reader, start=2):
            try:
                score = float(row["score"])
            except ValueError:
                print(f"ردیف {line_number} رد شد.")
                continue

            if row["passed"] == "yes":
                print(f"{row['name']}: {score}")


def solve_custom_delimiter_task():
    rows = [
        ["title", "note"],
        ["CSV", "متن شامل، ویرگول"],
        ["JSON", 'متن شامل "کوتیشن"'],
    ]

    with COURSES_FILE.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(rows)

    with COURSES_FILE.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file, delimiter=";")
        print("ردیف‌های فایل با جداکننده ;")
        for row in reader:
            print(row)


def solve_logging_task():
    logger = logging.getLogger("practice_log")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    logger.propagate = False

    handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(handler)

    logger.info("برنامه تمرین شروع شد")
    logger.warning("یک ردیف نامعتبر دیده شد")
    logger.error("یک خطای آموزشی ثبت شد")


def solve_orders_report_task():
    orders = [
        {"order_id": "1", "city": "تهران", "amount": "120000", "status": "paid"},
        {"order_id": "2", "city": "یزد", "amount": "80000", "status": "paid"},
        {"order_id": "3", "city": "تهران", "amount": "40000", "status": "canceled"},
        {"order_id": "4", "city": "یزد", "amount": "50000", "status": "paid"},
    ]

    with ORDERS_FILE.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["order_id", "city", "amount", "status"])
        writer.writeheader()
        writer.writerows(orders)

    city_totals = {}
    with ORDERS_FILE.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["status"] != "paid":
                continue

            city_totals[row["city"]] = city_totals.get(row["city"], 0) + int(row["amount"])

    report = {
        "city_totals": city_totals,
        "grand_total": sum(city_totals.values()),
    }
    REPORT_FILE.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"گزارش سفارش‌ها ساخته شد: {REPORT_FILE}")


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)
    solve_json_tasks()
    solve_students_csv_task()
    solve_custom_delimiter_task()
    solve_logging_task()
    solve_orders_report_task()


if __name__ == "__main__":
    main()
