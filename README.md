# کارگاه کار با فایل‌ها در پایتون

<p align="center" dir="ltr">
  <img alt="Python 3.10+" src="https://img.shields.io/badge/Python-3.10%2B-3776AB">
  <img alt="Standard library only" src="https://img.shields.io/badge/Standard%20library-only-2ea44f">
  <img alt="Persian documentation" src="https://img.shields.io/badge/Docs-Persian-blue">
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
└── .gitignore
```

نقش فایل‌های اصلی:

<table dir="rtl">
  <thead>
    <tr>
      <th>فایل</th>
      <th>نقش</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>فایل <span dir="ltr"><code>README.md</code></span></td>
      <td>راهنمای اصلی مخزن برای GitHub</td>
    </tr>
    <tr>
      <td>فایل <span dir="ltr"><code>Notes.txt</code></span></td>
      <td>طرح درس و توضیح مفاهیم برای مدرس یا خودخوانی</td>
    </tr>
    <tr>
      <td>فایل <span dir="ltr"><code>practice_tasks.md</code></span></td>
      <td>تمرین‌های مرحله‌ای از مقدماتی تا پروژه پایانی</td>
    </tr>
    <tr>
      <td>فایل <span dir="ltr"><code>practice_solution_beginner.py</code></span></td>
      <td>پاسخ نمونه تمرین‌های مقدماتی</td>
    </tr>
    <tr>
      <td>فایل <span dir="ltr"><code>practice_solution_intermediate.py</code></span></td>
      <td>پاسخ نمونه تمرین‌های میانی</td>
    </tr>
    <tr>
      <td>فایل <span dir="ltr"><code>practice_solution_advanced.py</code></span></td>
      <td>پاسخ نمونه تمرین‌های تکمیلی</td>
    </tr>
    <tr>
      <td>فایل <span dir="ltr"><code>practice_solution.py</code></span></td>
      <td>پاسخ نمونه پروژه پایانی</td>
    </tr>
    <tr>
      <td>پوشه <span dir="ltr"><code>workshop_output</code></span></td>
      <td>پوشه خروجی اجراها، در گیت ذخیره نمی‌شود</td>
    </tr>
  </tbody>
</table>

<a id="learning-path"></a>
## مسیر یادگیری

پیشنهاد می‌شود فایل‌ها با همین ترتیب اجرا شوند:

<table dir="rtl">
  <thead>
    <tr>
      <th>بخش</th>
      <th>نمونه‌ها</th>
      <th>تمرکز</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>پایه فایل متنی</td>
      <td>نمونه‌های <span dir="ltr"><code>example1.py</code></span> تا <span dir="ltr"><code>example5.py</code></span></td>
      <td>حالت‌های فایل، کدگذاری، خواندن خطی، context manager و مسیرها</td>
    </tr>
    <tr>
      <td>داده ساخت‌یافته</td>
      <td>نمونه‌های <span dir="ltr"><code>example6.py</code></span> تا <span dir="ltr"><code>example10.py</code></span></td>
      <td>قالب‌های <span dir="ltr"><code>JSON</code></span> و <span dir="ltr"><code>CSV</code></span>، لاگ و گزارش‌گیری</td>
    </tr>
    <tr>
      <td>خطا و ابزارهای فایل</td>
      <td>نمونه‌های <span dir="ltr"><code>example11.py</code></span>، <span dir="ltr"><code>example12.py</code></span> و <span dir="ltr"><code>example14.py</code></span> تا <span dir="ltr"><code>example18.py</code></span></td>
      <td>مدیریت خطا، باینری، نوشتن امن، پیمایش پوشه، zip، پردازش جریانی و INI</td>
    </tr>
    <tr>
      <td>پروژه پایانی</td>
      <td>نمونه <span dir="ltr"><code>example13.py</code></span></td>
      <td>خواندن CSV، فیلتر، لاگ و ساخت گزارش JSON</td>
    </tr>
  </tbody>
</table>

<a id="examples-table"></a>
## جدول نمونه‌ها

<table dir="rtl">
  <thead>
    <tr>
      <th>شماره</th>
      <th>فایل</th>
      <th>مفهوم اصلی</th>
      <th>خروجی مهم</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>فایل <span dir="ltr"><code>example1.py</code></span></td><td>حالت‌های <span dir="ltr"><code>r</code></span>، <span dir="ltr"><code>w</code></span>، <span dir="ltr"><code>a</code></span> و <span dir="ltr"><code>r+</code></span></td><td>فایل متنی <span dir="ltr"><code>modes.txt</code></span></td></tr>
    <tr><td>2</td><td>فایل <span dir="ltr"><code>example2.py</code></span></td><td>کدگذاری <span dir="ltr"><code>utf-8</code></span>، <span dir="ltr"><code>BOM</code></span> و خطای decode</td><td>فایل‌های متنی فارسی</td></tr>
    <tr><td>3</td><td>فایل <span dir="ltr"><code>example3.py</code></span></td><td>روش‌های <span dir="ltr"><code>read</code></span>، <span dir="ltr"><code>readline</code></span> و <span dir="ltr"><code>readlines</code></span></td><td>فایل چندخطی</td></tr>
    <tr><td>4</td><td>فایل <span dir="ltr"><code>example4.py</code></span></td><td>بستن خودکار فایل با context manager</td><td>فایل <span dir="ltr"><code>context_manager.txt</code></span></td></tr>
    <tr><td>5</td><td>فایل <span dir="ltr"><code>example5.py</code></span></td><td>مسیرها با <span dir="ltr"><code>pathlib.Path</code></span> و جست‌وجو با <span dir="ltr"><code>glob</code></span></td><td>پوشه نمونه مسیرها</td></tr>
    <tr><td>6</td><td>فایل <span dir="ltr"><code>example6.py</code></span></td><td>داده تو در تو و خطای JSON خراب</td><td>فایل <span dir="ltr"><code>profile.json</code></span></td></tr>
    <tr><td>7</td><td>فایل <span dir="ltr"><code>example7.py</code></span></td><td>خواندن و نوشتن CSV با سرستون</td><td>فایل <span dir="ltr"><code>people.csv</code></span></td></tr>
    <tr><td>8</td><td>فایل <span dir="ltr"><code>example8.py</code></span></td><td>جداکننده سفارشی و نقل‌قول در CSV</td><td>فایل <span dir="ltr"><code>courses_semicolon.csv</code></span></td></tr>
    <tr><td>9</td><td>فایل <span dir="ltr"><code>example9.py</code></span></td><td>سطح‌های لاگ و قالب پیام</td><td>فایل <span dir="ltr"><code>app.log</code></span></td></tr>
    <tr><td>10</td><td>فایل <span dir="ltr"><code>example10.py</code></span></td><td>فیلتر و تجمیع CSV در گزارش JSON</td><td>فایل <span dir="ltr"><code>sales_report.json</code></span></td></tr>
    <tr><td>11</td><td>فایل <span dir="ltr"><code>example11.py</code></span></td><td>خطاهای فایل با <span dir="ltr"><code>try</code></span>، <span dir="ltr"><code>except</code></span> و <span dir="ltr"><code>finally</code></span></td><td>خواندن امن فایل</td></tr>
    <tr><td>12</td><td>فایل <span dir="ltr"><code>example12.py</code></span></td><td>تفاوت فایل متنی و فایل باینری</td><td>فایل <span dir="ltr"><code>bytes_sample.bin</code></span></td></tr>
    <tr><td>13</td><td>فایل <span dir="ltr"><code>example13.py</code></span></td><td>پروژه پایانی، CSV، لاگ و گزارش JSON</td><td>فایل <span dir="ltr"><code>capstone_report.json</code></span></td></tr>
    <tr><td>14</td><td>فایل <span dir="ltr"><code>example14.py</code></span></td><td>نوشتن امن با فایل موقت و پشتیبان</td><td>فایل <span dir="ltr"><code>inventory.json</code></span></td></tr>
    <tr><td>15</td><td>فایل <span dir="ltr"><code>example15.py</code></span></td><td>پیمایش پوشه با <span dir="ltr"><code>rglob</code></span> و اندازه فایل‌ها</td><td>فایل <span dir="ltr"><code>directory_report.json</code></span></td></tr>
    <tr><td>16</td><td>فایل <span dir="ltr"><code>example16.py</code></span></td><td>ساخت و خواندن فایل zip</td><td>فایل <span dir="ltr"><code>archive_demo.zip</code></span></td></tr>
    <tr><td>17</td><td>فایل <span dir="ltr"><code>example17.py</code></span></td><td>پردازش جریانی CSV بزرگ با generator</td><td>فایل <span dir="ltr"><code>large_sales.csv</code></span></td></tr>
    <tr><td>18</td><td>فایل <span dir="ltr"><code>example18.py</code></span></td><td>فایل تنظیمات با <span dir="ltr"><code>configparser</code></span></td><td>فایل <span dir="ltr"><code>app.ini</code></span></td></tr>
  </tbody>
</table>

<a id="practice"></a>
## تمرین‌ها و پاسخ‌ها

فایل <span dir="ltr"><code>practice_tasks.md</code></span> تمرین‌ها را در پنج بخش مرتب کرده است.

<table dir="rtl">
  <thead>
    <tr>
      <th>سطح</th>
      <th>تمرین‌ها</th>
      <th>پاسخ نمونه</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>مقدماتی</td><td>تمرین‌های 1 تا 4</td><td>فایل <span dir="ltr"><code>practice_solution_beginner.py</code></span></td></tr>
    <tr><td>میانی</td><td>تمرین‌های 5 تا 10</td><td>فایل <span dir="ltr"><code>practice_solution_intermediate.py</code></span></td></tr>
    <tr><td>تکمیلی</td><td>تمرین‌های 14 تا 18</td><td>فایل <span dir="ltr"><code>practice_solution_advanced.py</code></span></td></tr>
    <tr><td>پروژه پایانی</td><td>تمرین 13</td><td>فایل <span dir="ltr"><code>practice_solution.py</code></span></td></tr>
  </tbody>
</table>

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

<table dir="rtl">
  <thead>
    <tr>
      <th>خطا</th>
      <th>معنی</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>خطای <span dir="ltr"><code>FileNotFoundError</code></span></td><td>مسیر فایل اشتباه است یا فایل هنوز ساخته نشده است.</td></tr>
    <tr><td>خطای <span dir="ltr"><code>PermissionError</code></span></td><td>برنامه اجازه خواندن یا نوشتن روی مسیر را ندارد.</td></tr>
    <tr><td>خطای <span dir="ltr"><code>UnicodeDecodeError</code></span></td><td>فایل با کدگذاری مورد انتظار خوانده نشده است.</td></tr>
    <tr><td>خطای <span dir="ltr"><code>json.JSONDecodeError</code></span></td><td>ساختار JSON خراب است.</td></tr>
    <tr><td>خطای <span dir="ltr"><code>ValueError</code></span></td><td>تبدیل مقدار متنی به عدد یا نوع دیگر ممکن نیست.</td></tr>
  </tbody>
</table>
