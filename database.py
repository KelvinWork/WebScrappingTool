import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook



def createWorkBook():
    wb = Workbook()
    dest_filename = 'Test1.xlsx'
    wb.save(filename=dest_filename)


def writeWorkBook(price, alphabet):
    wb = load_workbook(filename="Test1.xlsx")
    ws1 = wb.active
    ws1.title = "Sheet"  # sheet name

    cellBlock = alphabet
    cellNumber = 1
    #print("This is the Block letter {}".format(cellBlock))
    #print(cellBlock)
    #print("this is len {}".format(len(cellBlock)))
    itemsInCell = ws1["{}{}".format(cellBlock, cellNumber)].value
    print(type(itemsInCell))
    print(cellBlock)
    print(cellNumber)

    while (itemsInCell != None):

        itemsInCell = ws1['{}{}'.format(cellBlock, cellNumber)].value
        print("this is in itemInCell {}".format(itemsInCell))

        cellNumber += 1
        print(cellNumber)
        print(cellBlock)

        if (itemsInCell == None):
            ws1['{}{}'.format(cellBlock, (cellNumber - 1))] = price

            break

    #print("write function has been called")
    #print(cellNumber)
    wb.save(filename="Test1.xlsx")


def readWorkBook(cells):
    wb = load_workbook(filename="Test1.xlsx", )
    sheet_ranges = wb['Sheet']
    print(sheet_ranges[cells].value)
    theReturnString = "Get Good"
    return theReturnString


def testWrite():
    wb = load_workbook(filename="Test1.xlsx")
    ws1 = wb.active
    ws1.title = "Sheet"

    ws1['C2'] = "Hello WhaaT?"
    print("test function called")
    wb.save(filename="Test1.xlsx")




#readWorkBook("C6")

#writeWorkBook("89.90")









