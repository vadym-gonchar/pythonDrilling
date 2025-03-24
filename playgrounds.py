import csv
import json

with open('playgrounds.csv', encoding='utf-8') as file_in:
    data = csv.DictReader(file_in, delimiter=';')

    result = {}

    for line in data:
        admin_area = line['AdmArea']
        district = line['District']
        address = line['Address']

        if admin_area not in result:
            result[admin_area] = {}

        if district not in result[admin_area]:
            result[admin_area][district] = []

        result[admin_area][district].append(address)

with open('addresses.json', 'w', encoding='utf-8') as file_out:
    json.dump(result, file_out, indent=3, ensure_ascii=False)