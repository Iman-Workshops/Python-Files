"""حل نمونه پروژه پایانی کار با فایل‌ها.

خروجی مورد انتظار: ساخت CSV، ثبت لاگ، رد کردن ردیف نامعتبر، و ساخت گزارش JSON.
"""

import csv
import json
import logging
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
STUDENTS_FILE = OUTPUT_DIR / "practice_students.csv"
REPORT_FILE = OUTPUT_DIR / "practice_report.json"
LOG_FILE = OUTPUT_DIR / "practice_capstone.log"
FIELDNAMES = ["name", "score", "passed"]


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def build_logger():
    logger = logging.getLogger("practice_capstone")
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
        {"name": "علی", "score": "bad-score", "passed": "yes"},
        {"name": "نگار", "score": "16.75", "passed": "yes"},
    ]

    with STUDENTS_FILE.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def load_students(logger):
    passed_students = []
    skipped_rows = []
    total_rows = 0

    with STUDENTS_FILE.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for line_number, row in enumerate(reader, start=2):
            total_rows += 1
            try:
                score = float(row["score"])
            except (KeyError, TypeError, ValueError):
                skipped_rows.append(line_number)
                logger.warning("ردیف %s نمره معتبر ندارد", line_number)
                continue

            if row.get("passed", "").strip().lower() == "yes":
                passed_students.append({"name": row["name"], "score": score})

    return total_rows, passed_students, skipped_rows


def build_report(total_rows, passed_students, skipped_rows):
    if passed_students:
        average_score = round(
            sum(student["score"] for student in passed_students) / len(passed_students),
            2,
        )
        top_student = max(passed_students, key=lambda student: student["score"])
    else:
        average_score = 0
        top_student = None

    return {
        "total_rows": total_rows,
        "passed_count": len(passed_students),
        "average_score": average_score,
        "skipped_rows": skipped_rows,
        "top_student": top_student,
        "students": passed_students,
    }


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)
    logger = build_logger()

    write_sample_students()
    logger.info("فایل CSV نمونه ساخته شد")

    total_rows, passed_students, skipped_rows = load_students(logger)
    report = build_report(total_rows, passed_students, skipped_rows)
    REPORT_FILE.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    logger.info("گزارش JSON ساخته شد")

    print(f"فایل CSV: {STUDENTS_FILE}")
    print(f"فایل لاگ: {LOG_FILE}")
    print(f"گزارش JSON: {REPORT_FILE}")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
