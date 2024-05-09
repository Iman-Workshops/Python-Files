new_rows = [['سارا', 22, 'کرمان'], ['رضا', 28, 'یزد']]

# باز کردن فایل برای افزودن داده‌های جدید
with open('example.csv', 'a', encoding='utf-8', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(new_rows)

# توضیح دهید که csv.writer چگونه برای نوشتن ردیف‌های جدید به فایل‌های CSV استفاده می‌شود.