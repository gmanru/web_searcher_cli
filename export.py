import csv
import json


def mass_dict_to_csv(mass):

    with open('csv_output.csv', 'w') as f:

            w = csv.DictWriter(f, mass[0].keys())
            w.writeheader()
            for item in mass:
                w.writerow(item)

            print("csv файл был создан/изменен")

def mass_dict_to_json(mass):
    with open('json_output.json', 'w') as f:
        for item in mass:

            json.dump(item, f)

        print("json файл был создан/изменен")