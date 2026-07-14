"""آموزش پیمایش پوشه، rglob، stat و ساخت فهرست فایل‌ها.

خروجی مورد انتظار: ساخت چند فایل و تولید directory_report.json با اندازه هر فایل.
"""

import json
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
PROJECT_DIR = OUTPUT_DIR / "directory_inventory"
REPORT_FILE = OUTPUT_DIR / "directory_report.json"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def create_sample_tree():
    files = {
        PROJECT_DIR / "notes" / "intro.txt": "یادداشت شروع کارگاه\n",
        PROJECT_DIR / "notes" / "summary.txt": "جمع‌بندی کوتاه\n",
        PROJECT_DIR / "data" / "scores.csv": "name,score\nSara,18\nReza,14\n",
        PROJECT_DIR / "data" / "readme.md": "# داده تمرینی\n",
    }

    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def build_inventory():
    records = []

    for path in sorted(PROJECT_DIR.rglob("*")):
        if not path.is_file():
            continue

        records.append(
            {
                "relative_path": str(path.relative_to(PROJECT_DIR)),
                "suffix": path.suffix,
                "size_bytes": path.stat().st_size,
            }
        )

    return records


def main():
    configure_stdout()
    create_sample_tree()

    records = build_inventory()
    report = {
        "file_count": len(records),
        "total_bytes": sum(record["size_bytes"] for record in records),
        "files": records,
    }
    REPORT_FILE.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"گزارش پوشه ساخته شد: {REPORT_FILE}")
    for record in records:
        print(f"{record['relative_path']}: {record['size_bytes']} بایت")


if __name__ == "__main__":
    main()
