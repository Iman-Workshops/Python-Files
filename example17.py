"""آموزش پردازش جریانی CSV بزرگ با generator.

خروجی مورد انتظار: ساخت large_sales.csv و محاسبه جمع فروش بدون نگه داشتن همه ردیف‌ها.
"""

import csv
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
SALES_FILE = OUTPUT_DIR / "large_sales.csv"
FIELDNAMES = ["order_id", "city", "amount", "status"]


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def write_large_sample():
    cities = ["تهران", "شیراز", "یزد", "رشت"]

    with SALES_FILE.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for number in range(1, 1001):
            writer.writerow(
                {
                    "order_id": number,
                    "city": cities[number % len(cities)],
                    "amount": 10000 + number,
                    "status": "paid" if number % 5 else "canceled",
                }
            )


def iter_paid_orders(path):
    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["status"] == "paid":
                yield row


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)
    write_large_sample()

    paid_count = 0
    total_amount = 0

    for row in iter_paid_orders(SALES_FILE):
        paid_count += 1
        total_amount += int(row["amount"])

    print(f"فایل CSV بزرگ ساخته شد: {SALES_FILE}")
    print(f"تعداد سفارش پرداخت شده: {paid_count}")
    print(f"جمع مبلغ سفارش‌های پرداخت شده: {total_amount}")


if __name__ == "__main__":
    main()
