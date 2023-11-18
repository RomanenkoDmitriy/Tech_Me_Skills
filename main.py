import json
import csv
from openpyxl import Workbook

# person = {111111: ("Ivan", 20),
#           222222: ("Ira",19),
#           333333: ("Vova", 40),
#           444444: ("Nina", 38),
#           555555: ("Igor", 15)}
# #
# with open("person.json", "w") as file:
#     json.dump(person, file, ensure_ascii=False, indent=4)


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


csv_person = []

with open("person.csv", "r") as f:
    fieldnames = ["id", "name", "age", "phone"]
    per = csv.DictReader(f, fieldnames=fieldnames)
    for i in per:
        csv_person.append(i)

print(csv_person)
wb = Workbook()
ws = wb.active

ws["B1"] = "person1"
ws["C1"] = "person2"
ws["D1"] = "person3"
ws["E1"] = "person4"
ws["F1"] = "person5"

ws["A2"] = "id"
ws["A3"] = "name"
ws["A4"] = "phone"

ws["B2"] = csv_person[0]["id"]
ws["C2"] = csv_person[1]["id"]
ws["D2"] = csv_person[2]["id"]
ws["E2"] = csv_person[3]["id"]
ws["F2"] = csv_person[4]["id"]

ws["B3"] = csv_person[0]["name"]
ws["C3"] = csv_person[1]["name"]
ws["D3"] = csv_person[2]["name"]
ws["E3"] = csv_person[3]["name"]
ws["F3"] = csv_person[4]["name"]

ws["B4"] = csv_person[0]["phone"]
ws["C4"] = csv_person[1]["phone"]
ws["D4"] = csv_person[2]["phone"]
ws["E4"] = csv_person[3]["phone"]
ws["F4"] = csv_person[4]["phone"]

wb.save("persons.xlsx")
