data['new_key'] = 'new_value'

# باز کردن فایل برای نوشتن داده‌های جدید
with open('example.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# توضیح دهید که چگونه می‌توان داده‌های دیکشنری را به فرمت JSON تبدیل و در فایل ذخیره کرد.