"""آموزش فایل تنظیمات INI با configparser.

خروجی مورد انتظار: ساخت app.ini، خواندن مقدارها و تغییر یک تنظیم.
"""

import configparser
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "workshop_output"
CONFIG_FILE = OUTPUT_DIR / "app.ini"


def configure_stdout():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")


def write_config():
    config = configparser.ConfigParser()
    config["app"] = {
        "language": "fa",
        "autosave": "yes",
        "theme": "light",
    }
    config["paths"] = {
        "output_dir": str(OUTPUT_DIR),
        "log_file": "app.log",
    }

    with CONFIG_FILE.open("w", encoding="utf-8") as file:
        config.write(file)


def main():
    configure_stdout()
    OUTPUT_DIR.mkdir(exist_ok=True)
    write_config()

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE, encoding="utf-8")

    autosave = config.getboolean("app", "autosave")
    language = config["app"]["language"]
    config["app"]["theme"] = "dark"

    with CONFIG_FILE.open("w", encoding="utf-8") as file:
        config.write(file)

    print(f"فایل تنظیمات ساخته شد: {CONFIG_FILE}")
    print(f"زبان برنامه: {language}")
    print(f"ذخیره خودکار فعال است؟ {autosave}")
    print("تنظیم theme به dark تغییر کرد.")


if __name__ == "__main__":
    main()
