"""آموزش ساخت و خواندن فایل zip با کتابخانه استاندارد.

خروجی مورد انتظار: ساخت archive_demo.zip و نمایش فهرست فایل‌های داخل آن.
"""

import sys
import zipfile
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
ZIP_SOURCE_DIR = OUTPUT_DIR / "zip_source"
ZIP_FILE = OUTPUT_DIR / "archive_demo.zip"
EXTRACT_DIR = OUTPUT_DIR / "zip_extracted"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def create_source_files():
    ZIP_SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    (ZIP_SOURCE_DIR / "lesson.txt").write_text("فایل متنی داخل zip\n", encoding="utf-8")
    (ZIP_SOURCE_DIR / "data.csv").write_text("name,score\nSara,18\n", encoding="utf-8")


def make_zip():
    with zipfile.ZipFile(ZIP_FILE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(ZIP_SOURCE_DIR.iterdir()):
            archive.write(path, arcname=path.name)


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)
    create_source_files()
    make_zip()

    with zipfile.ZipFile(ZIP_FILE, "r") as archive:
        names = archive.namelist()
        archive.extractall(EXTRACT_DIR)

    print(f"فایل zip ساخته شد: {ZIP_FILE}")
    print("فایل‌های داخل zip:")
    for name in names:
        print(f"- {name}")
    print(f"فایل‌ها در این پوشه باز شدند: {EXTRACT_DIR}")


if __name__ == "__main__":
    main()
