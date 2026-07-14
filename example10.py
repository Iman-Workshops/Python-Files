"""آموزش فیلتر، تبدیل نوع و تجمیع داده از CSV به گزارش JSON.

خروجی مورد انتظار: ساخت orders.csv و sales_report.json با جمع فروش هر شهر.
"""

import csv
import json
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
ORDERS_FILE = OUTPUT_DIR / "orders.csv"
REPORT_FILE = OUTPUT_DIR / "sales_report.json"
FIELDNAMES = ["order_id", "city", "amount", "status"]


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def write_orders():
    orders = [
        {"order_id": "1001", "city": "تهران", "amount": "250000", "status": "paid"},
        {"order_id": "1002", "city": "شیراز", "amount": "185000", "status": "paid"},
        {"order_id": "1003", "city": "تهران", "amount": "99000", "status": "canceled"},
        {"order_id": "1004", "city": "یزد", "amount": "320000", "status": "paid"},
        {"order_id": "1005", "city": "شیراز", "amount": "145000", "status": "paid"},
    ]

    with ORDERS_FILE.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(orders)


def build_report():
    city_totals = {}
    paid_count = 0

    with ORDERS_FILE.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["status"] != "paid":
                continue

            amount = int(row["amount"])
            city = row["city"]
            city_totals[city] = city_totals.get(city, 0) + amount
            paid_count += 1

    return {
        "paid_order_count": paid_count,
        "city_totals": city_totals,
        "grand_total": sum(city_totals.values()),
    }


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)
    write_orders()

    report = build_report()
    REPORT_FILE.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"فایل ورودی ساخته شد: {ORDERS_FILE}")
    print(f"گزارش ساخته شد: {REPORT_FILE}")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
