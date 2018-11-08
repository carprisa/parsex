import openpyxl

if __name__ == "__main__":
    # filename = your .xlsx file
    cn = openpyxl.load_workbook(filename="")

    print(type(cn))

    ws = cn.active
    print(ws)

    colG = ws['G']
    if colG[0].value == "Objeto":
        for cell in colG:
            print (cell.value)
            
    # type of the data should be a tuple
    print(type(colG))
