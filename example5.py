# مثلاً فیلتر کردن و نمایش تنها ردیف‌های CSV که سن بیشتر از 25 سال دارند
with open('example.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[1].isdigit() and int(row[1]) > 25:
            print(row)