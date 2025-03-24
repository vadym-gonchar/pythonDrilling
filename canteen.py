import json

with open('food_services.json', encoding='utf-8') as file_in:
    data = json.load(file_in)
    my_dict = {}

    for d in data:
        my_dict.setdefault(d['TypeObject'], []).append((d['Name'], d['SeatsCount']))
    res = {key: sorted(value, key=lambda x: -x[1]) for key, value in my_dict.items()}
    result = {}
    for key, value in res.items():
        result.setdefault(key, []).append((value[0][0], value[0][1]))

    final_res = sorted(result.items(), key=lambda x:x)

    for key, value in final_res:
        print(f"{key}: {value[0][0]}, {value[0][1]}")