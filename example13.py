"""پروژه پایانی: خواندن CSV، فیلتر، لاگ و ساخت گزارش JSON.

خروجی مورد انتظار: ساخت students_capstone.csv، capstone.log و capstone_report.json.
"""

import csv
import json
import logging
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
STUDENTS_FILE = OUTPUT_DIR / "students_capstone.csv"
REPORT_FILE = OUTPUT_DIR / "capstone_report.json"
LOG_FILE = OUTPUT_DIR / "capstone.log"
FIELDNAMES = ["name", "score", "passed"]


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def build_logger():
    logger = logging.getLogger("workshop_capstone")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    logger.propagate = False

    handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(handler)
    return logger


def write_sample_students():
    rows = [
        {"name": "سارا", "score": "18.5", "passed": "yes"},
        {"name": "رضا", "score": "14", "passed": "yes"},
        {"name": "مریم", "score": "9.5", "passed": "no"},
        {"name": "علی", "score": "not-number", "passed": "yes"},
        {"name": "نگار", "score": "16.75", "passed": "yes"},
    ]

    with STUDENTS_FILE.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def load_passed_students(logger):
    passed_students = []
    skipped_rows = []

    with STUDENTS_FILE.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for line_number, row in enumerate(reader, start=2):
            try:
                score = float(row["score"])
            except (KeyError, TypeError, ValueError):
                skipped_rows.append(line_number)
                logger.warning("ردیف %s به دلیل نمره نامعتبر رد شد", line_number)
                continue

            if row.get("passed", "").strip().lower() == "yes":
                passed_students.append({"name": row["name"], "score": score})

    return passed_students, skipped_rows


def build_report(passed_students, skipped_rows):
    if passed_students:
        average = round(
            sum(student["score"] for student in passed_students) / len(passed_students),
            2,
        )
    else:
        average = 0

    return {
        "passed_count": len(passed_students),
        "average_score": average,
        "skipped_rows": skipped_rows,
        "students": passed_students,
    }


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)
    logger = build_logger()

    write_sample_students()
    logger.info("فایل CSV نمونه ساخته شد")

    passed_students, skipped_rows = load_passed_students(logger)
    report = build_report(passed_students, skipped_rows)

    REPORT_FILE.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    logger.info("گزارش JSON ساخته شد")

    print(f"فایل ورودی: {STUDENTS_FILE}")
    print(f"گزارش: {REPORT_FILE}")
    print(f"لاگ: {LOG_FILE}")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
