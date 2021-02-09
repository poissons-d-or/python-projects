import csv
import pprint
from openpyxl import load_workbook
wb = load_workbook(filename='プローブ重量リスト.xlsx')
ws_pin = wb['PIN']
ws_bush = wb['BUSH']
ws_sr = wb['SR']
ws_sp = wb['SP']

# pinData = []
# bushNames = []
# srNames = []
# spNames = []

with open('./pinData.csv', 'w') as f:
    writer = csv.writer(f)
    for row in ws_pin.values:
        writer.writerow(row)

with open('./bushData.csv', 'w') as f:
    writer = csv.writer(f)
    for row in ws_bush.values:
        writer.writerow(row)

with open('./srData.csv', 'w') as f:
    writer = csv.writer(f)
    for row in ws_sr.values:
        writer.writerow(row)

with open('./spData.csv', 'w') as f:
    writer = csv.writer(f)
    for row in ws_sp.values:
        writer.writerow(row)

# for cell in ws_bush['A']:
        # bushNames.append(cell.value)

# for cell in ws_sr['A']:
        # srNames.append(cell.value)

# for cell in ws_sp['A']:
        # spNames.append(cell.value)

# print(list(dict.fromkeys(pinData)))
