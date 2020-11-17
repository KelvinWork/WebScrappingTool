import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook



def CreateWorkBook():
    wb = Workbook()
    dest_filename = 'Test1.xlsx'
    wb.save(filename=dest_filename)





wb = load_workbook(filename="Test1.xlsx", )

ws1 = wb.active

# ws1['F4'] = 3.14
# ws1['A1'] = "Hello World"
# wb.save(filename="Test1.xlsx")

sheet_ranges = wb['Sheet']
cellValue = sheet_ranges['F4'].value
print(cellValue)
print(type(cellValue))
nextCell =6

# if cellValue == None:
#     nextCell += 1
#     print("cellValue != None has been entered")
#
#
# elif cellValue ==None:
#     #ws1["C{}".format(nextCell)] = "Test1"
#     ws1["F2"] = "Hello World"
#     wb.save(filename="Test1.xlsx")
#     print("cellValue == None has been entered")
#
# else:



ws1["C{}".format(nextCell)] = "Test1"
wb.save(filename="Test1.xlsx")
print("cellValue == None has been s")


print(nextCell)
print("C{}".format(nextCell))


