import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook



def createWorkBook():
    wb = Workbook()
    dest_filename = 'Test1.xlsx'
    wb.save(filename=dest_filename)


def writeWorkBook(price):
    wb = load_workbook(filename="Test1.xlsx")
    ws1 = wb.active
    ws1.title = "Sheet"  # sheet name

    cellBlock = "A"
    cellNumber = 1

    itemsInCell = ws1["{}{}".format(cellBlock, cellNumber)].value
    print(type(itemsInCell))

    while (itemsInCell != None):

        itemsInCell = ws1["{}{}".format(cellBlock, cellNumber)].value
        print(type(itemsInCell))

        cellNumber += 1
        print(cellNumber)

        if (itemsInCell == None):
            ws1["{}{}".format(cellBlock, cellNumber - 1)] = price
            break

    print("write function has been called")
    print(cellNumber)
    wb.save(filename="Test1.xlsx")


def readWorkBook(cells):
    wb = load_workbook(filename="Test1.xlsx", )
    sheet_ranges = wb['Sheet']
    print(sheet_ranges[cells].value)
    theReturnString = "Get Good"
    return theReturnString

#readWorkBook("C6")
#writeWorkBook("89.90")









