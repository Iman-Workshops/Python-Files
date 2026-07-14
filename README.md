# کارگاه کار با فایل‌ها در پایتون

<p align="center" dir="ltr">
  <img alt="Python 3.10+" src="https://img.shields.io/badge/Python-3.10%2B-3776AB">
  <img alt="Standard library only" src="https://img.shields.io/badge/Standard%20library-only-2ea44f">
  <img alt="Persian documentation" src="https://img.shields.io/badge/Docs-Persian-blue">
  <img alt="MIT license" src="https://img.shields.io/badge/License-MIT-yellow">
</p>

این مخزن یک منبع آموزشی فارسی برای یادگیری کار با فایل‌ها در پایتون است. مسیر یادگیری از فایل متنی ساده شروع می‌شود و به داده ساخت‌یافته، لاگ، مدیریت خطا، فایل باینری، آرشیو، پردازش جریانی و پروژه پایانی می‌رسد.

همه نمونه‌ها مستقل اجرا می‌شوند، فقط به کتابخانه استاندارد پایتون نیاز دارند و خروجی خود را در پوشه <span dir="ltr"><code>workshop_output</code></span> می‌سازند.

## فهرست مطالب

- [معرفی پروژه](#overview)
- [پیش نیاز](#requirements)
- [شروع سریع](#quick-start)
- [ساختار مخزن](#repository-structure)
- [مسیر یادگیری](#learning-path)
- [جدول نمونه‌ها](#examples-table)
- [تمرین‌ها و پاسخ‌ها](#practice)
- [نکته‌های آموزشی](#teaching-notes)
- [خطاهای رایج](#common-errors)
- [مجوز](#license)

<a id="overview"></a>
## معرفی پروژه

هدف این کارگاه این است که دانشجو بتواند فایل را فقط به چشم یک ورودی یا خروجی ساده نبیند. در یک برنامه واقعی، فایل می‌تواند تنظیمات، داده جدولی، گزارش، لاگ، آرشیو، خروجی تحلیل یا داده باینری باشد.

موضوع‌های اصلی این مخزن:

- حالت‌های باز کردن فایل، شامل <span dir="ltr"><code>r</code></span>، <span dir="ltr"><code>w</code></span>، <span dir="ltr"><code>a</code></span>، <span dir="ltr"><code>x</code></span> و <span dir="ltr"><code>r+</code></span>
- مدیریت فایل با <span dir="ltr"><code>with open(...)</code></span>
- خواندن خط به خط برای فایل‌های بزرگ
- کدگذاری <span dir="ltr"><code>utf-8</code></span> برای متن فارسی، فایل دارای <span dir="ltr"><code>BOM</code></span> و خطاهای decode
- مسیرهای قابل حمل با <span dir="ltr"><code>pathlib.Path</code></span>
- خواندن و نوشتن داده با <span dir="ltr"><code>JSON</code></span> و <span dir="ltr"><code>CSV</code></span>
- ثبت رخدادها با ماژول <span dir="ltr"><code>logging</code></span>
- مدیریت خطاهای رایج فایل
- تفاوت فایل متنی و باینری
- نوشتن امن با فایل موقت و جایگزینی اتمی
- پیمایش پوشه، ساخت فایل <span dir="ltr"><code>zip</code></span>، پردازش جریانی و فایل تنظیمات <span dir="ltr"><code>INI</code></span>

<a id="requirements"></a>
## پیش نیاز

برای اجرای کدها این موارد کافی است:

- نسخه <span dir="ltr"><code>Python 3.10</code></span> یا نسخه جدیدتر
- آشنایی مقدماتی با رشته، لیست، دیکشنری، شرط و حلقه
- ترمینال یا محیطی که دستور <span dir="ltr"><code>python</code></span> را اجرا کند

برای بررسی نسخه پایتون:

```bash
python --version
```

هیچ بسته جانبی لازم نیست.

<a id="quick-start"></a>
## شروع سریع

ابتدا مخزن را دریافت کنید:

```bash
git clone https://github.com/Iman-Workshops/Python-Files.git
cd Python-Files
```

سپس هر نمونه را جداگانه اجرا کنید:

```bash
python example1.py
python example2.py
python example3.py
python example4.py
python example5.py
python example6.py
python example7.py
python example8.py
python example9.py
python example10.py
python example11.py
python example12.py
python example13.py
python example14.py
python example15.py
python example16.py
python example17.py
python example18.py
```

برای اجرای پاسخ‌های نمونه:

```bash
python practice_solution_beginner.py
python practice_solution_intermediate.py
python practice_solution_advanced.py
python practice_solution.py
```

<a id="repository-structure"></a>
## ساختار مخزن

```text
.
├── README.md
├── Notes.txt
├── practice_tasks.md
├── practice_solution.py
├── practice_solution_beginner.py
├── practice_solution_intermediate.py
├── practice_solution_advanced.py
├── example1.py
├── example2.py
├── ...
├── example18.py
├── LICENSE
└── .gitignore
```

نقش فایل‌های اصلی:

| فایل | نقش |
| --- | --- |
| <span dir="ltr"><code>README.md</code></span> | راهنمای اصلی مخزن برای GitHub |
| <span dir="ltr"><code>Notes.txt</code></span> | طرح درس و توضیح مفاهیم برای مدرس یا خودخوانی |
| <span dir="ltr"><code>practice_tasks.md</code></span> | تمرین‌های مرحله‌ای از مقدماتی تا پروژه پایانی |
| <span dir="ltr"><code>practice_solution_beginner.py</code></span> | پاسخ نمونه تمرین‌های مقدماتی |
| <span dir="ltr"><code>practice_solution_intermediate.py</code></span> | پاسخ نمونه تمرین‌های میانی |
| <span dir="ltr"><code>practice_solution_advanced.py</code></span> | پاسخ نمونه تمرین‌های تکمیلی |
| <span dir="ltr"><code>practice_solution.py</code></span> | پاسخ نمونه پروژه پایانی |
| <span dir="ltr"><code>workshop_output</code></span> | پوشه خروجی اجراها، در گیت ذخیره نمی‌شود |

<a id="learning-path"></a>
## مسیر یادگیری

پیشنهاد می‌شود فایل‌ها با همین ترتیب اجرا شوند:

| بخش | نمونه‌ها | تمرکز |
| --- | --- | --- |
| پایه فایل متنی | <span dir="ltr"><code>example1.py</code></span> تا <span dir="ltr"><code>example5.py</code></span> | حالت‌های فایل، کدگذاری، خواندن خطی، context manager و مسیرها |
| داده ساخت‌یافته | <span dir="ltr"><code>example6.py</code></span> تا <span dir="ltr"><code>example10.py</code></span> | قالب‌های <span dir="ltr"><code>JSON</code></span> و <span dir="ltr"><code>CSV</code></span>، لاگ و گزارش‌گیری |
| خطا و ابزارهای فایل | <span dir="ltr"><code>example11.py</code></span>، <span dir="ltr"><code>example12.py</code></span> و <span dir="ltr"><code>example14.py</code></span> تا <span dir="ltr"><code>example18.py</code></span> | مدیریت خطا، باینری، نوشتن امن، پیمایش پوشه، zip، پردازش جریانی و INI |
| پروژه پایانی | <span dir="ltr"><code>example13.py</code></span> | خواندن CSV، فیلتر، لاگ و ساخت گزارش JSON |

<a id="examples-table"></a>
## جدول نمونه‌ها

| شماره | فایل | مفهوم اصلی | خروجی مهم |
| --- | --- | --- | --- |
| 1 | <span dir="ltr"><code>example1.py</code></span> | حالت‌های <span dir="ltr"><code>r</code></span>، <span dir="ltr"><code>w</code></span>، <span dir="ltr"><code>a</code></span> و <span dir="ltr"><code>r+</code></span> | فایل متنی <span dir="ltr"><code>modes.txt</code></span> |
| 2 | <span dir="ltr"><code>example2.py</code></span> | کدگذاری <span dir="ltr"><code>utf-8</code></span>، <span dir="ltr"><code>BOM</code></span> و خطای decode | فایل‌های متنی فارسی |
| 3 | <span dir="ltr"><code>example3.py</code></span> | روش‌های <span dir="ltr"><code>read</code></span>، <span dir="ltr"><code>readline</code></span> و <span dir="ltr"><code>readlines</code></span> | فایل چندخطی |
| 4 | <span dir="ltr"><code>example4.py</code></span> | بستن خودکار فایل با context manager | فایل <span dir="ltr"><code>context_manager.txt</code></span> |
| 5 | <span dir="ltr"><code>example5.py</code></span> | مسیرها با <span dir="ltr"><code>pathlib.Path</code></span> و جست‌وجو با <span dir="ltr"><code>glob</code></span> | پوشه نمونه مسیرها |
| 6 | <span dir="ltr"><code>example6.py</code></span> | داده تو در تو و خطای JSON خراب | فایل <span dir="ltr"><code>profile.json</code></span> |
| 7 | <span dir="ltr"><code>example7.py</code></span> | خواندن و نوشتن CSV با سرستون | فایل <span dir="ltr"><code>people.csv</code></span> |
| 8 | <span dir="ltr"><code>example8.py</code></span> | جداکننده سفارشی و نقل‌قول در CSV | فایل <span dir="ltr"><code>courses_semicolon.csv</code></span> |
| 9 | <span dir="ltr"><code>example9.py</code></span> | سطح‌های لاگ و قالب پیام | فایل <span dir="ltr"><code>app.log</code></span> |
| 10 | <span dir="ltr"><code>example10.py</code></span> | فیلتر و تجمیع CSV در گزارش JSON | فایل <span dir="ltr"><code>sales_report.json</code></span> |
| 11 | <span dir="ltr"><code>example11.py</code></span> | خطاهای فایل با <span dir="ltr"><code>try</code></span>، <span dir="ltr"><code>except</code></span> و <span dir="ltr"><code>finally</code></span> | خواندن امن فایل |
| 12 | <span dir="ltr"><code>example12.py</code></span> | تفاوت فایل متنی و فایل باینری | فایل <span dir="ltr"><code>bytes_sample.bin</code></span> |
| 13 | <span dir="ltr"><code>example13.py</code></span> | پروژه پایانی، CSV، لاگ و گزارش JSON | فایل <span dir="ltr"><code>capstone_report.json</code></span> |
| 14 | <span dir="ltr"><code>example14.py</code></span> | نوشتن امن با فایل موقت و پشتیبان | فایل <span dir="ltr"><code>inventory.json</code></span> |
| 15 | <span dir="ltr"><code>example15.py</code></span> | پیمایش پوشه با <span dir="ltr"><code>rglob</code></span> و اندازه فایل‌ها | فایل <span dir="ltr"><code>directory_report.json</code></span> |
| 16 | <span dir="ltr"><code>example16.py</code></span> | ساخت و خواندن فایل zip | فایل <span dir="ltr"><code>archive_demo.zip</code></span> |
| 17 | <span dir="ltr"><code>example17.py</code></span> | پردازش جریانی CSV بزرگ با generator | فایل <span dir="ltr"><code>large_sales.csv</code></span> |
| 18 | <span dir="ltr"><code>example18.py</code></span> | فایل تنظیمات با <span dir="ltr"><code>configparser</code></span> | فایل <span dir="ltr"><code>app.ini</code></span> |

<a id="practice"></a>
## تمرین‌ها و پاسخ‌ها

فایل <span dir="ltr"><code>practice_tasks.md</code></span> تمرین‌ها را در پنج بخش مرتب کرده است.

| سطح | تمرین‌ها | پاسخ نمونه |
| --- | --- | --- |
| مقدماتی | تمرین‌های 1 تا 4 | <span dir="ltr"><code>practice_solution_beginner.py</code></span> |
| میانی | تمرین‌های 5 تا 10 | <span dir="ltr"><code>practice_solution_intermediate.py</code></span> |
| تکمیلی | تمرین‌های 14 تا 18 | <span dir="ltr"><code>practice_solution_advanced.py</code></span> |
| پروژه پایانی | تمرین 13 | <span dir="ltr"><code>practice_solution.py</code></span> |

<a id="teaching-notes"></a>
## نکته‌های آموزشی

- حالت <span dir="ltr"><code>w</code></span> فایل قبلی را پاک می‌کند.
- حالت <span dir="ltr"><code>a</code></span> داده را به انتهای فایل اضافه می‌کند.
- حالت <span dir="ltr"><code>r+</code></span> به مکان نشانگر فایل وابسته است.
- برای متن فارسی، کدگذاری <span dir="ltr"><code>utf-8</code></span> باید روشن نوشته شود.
- برای فایل بزرگ، حلقه روی شی فایل از <span dir="ltr"><code>read</code></span> و <span dir="ltr"><code>readlines</code></span> مناسب‌تر است.
- عبارت <span dir="ltr"><code>with</code></span> فایل را حتی هنگام خطا می‌بندد.
- گزینه <span dir="ltr"><code>newline=""</code></span> هنگام کار با CSV از خط خالی ناخواسته جلوگیری می‌کند.
- ماژول <span dir="ltr"><code>logging</code></span> برای ثبت رخدادهای برنامه از <span dir="ltr"><code>print</code></span> مناسب‌تر است.

<a id="common-errors"></a>
## خطاهای رایج

| خطا | معنی |
| --- | --- |
| <span dir="ltr"><code>FileNotFoundError</code></span> | مسیر فایل اشتباه است یا فایل هنوز ساخته نشده است. |
| <span dir="ltr"><code>PermissionError</code></span> | برنامه اجازه خواندن یا نوشتن روی مسیر را ندارد. |
| <span dir="ltr"><code>UnicodeDecodeError</code></span> | فایل با کدگذاری مورد انتظار خوانده نشده است. |
| <span dir="ltr"><code>json.JSONDecodeError</code></span> | ساختار JSON خراب است. |
| <span dir="ltr"><code>ValueError</code></span> | تبدیل مقدار متنی به عدد یا نوع دیگر ممکن نیست. |

<a id="license"></a>
## مجوز

این پروژه با مجوز <span dir="ltr"><code>MIT</code></span> منتشر شده است. متن کامل مجوز در فایل <span dir="ltr"><code>LICENSE</code></span> قرار دارد.
