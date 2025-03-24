import csv
import json

with open('data.json', encoding='utf-8') as file_in:
    data = json.load(file_in)
    lst = []
    for line in data:
        if line['age'] >= 18 and line['progress'] >= 75:
            lst.append(line)
    lst = sorted(lst, key=lambda x: x['name'])
    print(lst)

with open('data.csv', 'w', encoding='utf-8', newline='') as file:
    fieldnames = ['name', 'phone']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for i in lst:
        writer.writerow({'name':i['name'], 'phone':i['phone']})