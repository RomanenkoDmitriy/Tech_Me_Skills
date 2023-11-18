import json
import csv
from openpyxl import Workbook, load_workbook

# person = {111111: ("Ivan", 20),
#           222222: ("Ira",19),
#           333333: ("Vova", 40),
#           444444: ("Nina", 38),
#           555555: ("Igor", 15)}
# #
# with open("person.json", "w") as file:
#     json.dump(person, file, ensure_ascii=False, indent=4)


# with open("person.json", "r") as file_json:
#     person = json.load(file_json)
#
# # print(person)
# person_phone = [99999999, 88888888, 77777777, 66666666, 55555555]
# list_person = []
# c = 1
# for k, v in person.items():
#     list_person.append({"id": k, "name": v[0], "age": v[1], "phone": person_phone[c - 1]})
#     c += 1
# # print(list_person)
#
# with open("person.csv", "w") as file_csv:
#     fieldnames = ["id", "name", "age", "phone"]
#     writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
#     for row in list_person:
#         writer.writerow(row)
#
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
