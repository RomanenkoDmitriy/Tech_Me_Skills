import json
import csv
from openpyxl import Workbook

person = {111111: ("Ivan", 20),
          222222: ("Ira", 19),
          333333: ("Vova", 40),
          444444: ("Nina", 38),
          555555: ("Igor", 15)}

with open("person.json", "w") as file:
    json.dump(person, file, ensure_ascii=False, indent=4)

with open("person.json", "r") as file_json:
    person = json.load(file_json)

person_phone = [99999999, 88888888, 77777777, 66666666, 55555555]

with open("person.csv", "w") as file_csv:
    fieldnames = ["id", "name", "age", "phone"]
    writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
    writer.writeheader()
    for i, p in zip(person, person_phone):
        writer.writerow({fieldnames[0]: i, fieldnames[1]: person[i][0],
                         fieldnames[2]: person[i][1], fieldnames[3]: p})

wb = Workbook()
ws = wb.active

col_dict = {}

with open("person.csv", "r") as csv_file:
    file_reader = csv.DictReader(csv_file)
    for i in range(2, 7):
        ws.cell(row=1, column=i).value = f"Person {i - 1}"
    col_dict = {"id": [], "name": [], "phone": []}
    for i in file_reader:
        for j in i:
            if j in col_dict:
                col_dict[j].append(i[j])
    print(col_dict)
for i in col_dict:
    ws.append([i] + col_dict[i])

wb.save("person.xlsx")
