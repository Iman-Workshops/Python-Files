# باز کردن فایل برای افزودن ورودی جدید
with open('example.log', 'a', encoding='utf-8') as file:
    file.write('2023-05-02 10:00:00 INFO New entry added.\n')

# توضیح دهید که چگونه می‌توان اطلاعات جدیدی را به فایل لاگ افزود.