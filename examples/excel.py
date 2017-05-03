def pyexcel_ex(input_file):
    print("[==== pyexcel example ====]") 
    import pyexcel as pe
    records = pe.iget_records(file_name=input_file)

    # Using pyexcel is preferable because it will automatically create a dictionary
    # of each row that uses the 1st row column values as the keys
    for record in records:
        print("{}'s phone # is {}".format(record['Place'], record['Phone #']))

    raw_input("Press Enter to next example...")

def openpyxl_ex(input_file):
    print("[==== openpyxl example ====]") 
    from openpyxl import load_workbook
    wb = load_workbook(input_file, read_only=True)
    print("Sheet names={}".format(wb.get_sheet_names()))

    ws = wb['Sheet1']

    for row in ws.rows:
        for cell in row:
            print(cell.value)
            
    # As far as I know, openpyxl cannot access values using a dictionary 
    # structure like pyexcel
    print("Cell A1={}".format(ws['A1'].value))

excel_file = "houston_places.xlsx"
        
pyexcel_ex(excel_file)
openpyxl_ex(excel_file)
