import openpyxl
import os

wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'].value = 'Lalle'
sheet2 = wb.create_sheet()
sheet2['A1'].value='Paneer Butter Masala'
print(sheet['A1'].value == 'Lalle')

os.mkdir('./openpyxlfiles/')
wb.save('./openpyxlfiles/lalle.xlsx')