import pandas
import xlwt

from srblib import abs_path

def excel_to_data(inp_path):
    inp_path = abs_path(inp_path)
    raw_data = pandas.read_excel(inp_path)
    header = list(raw_data.columns)

    if(len(header) == 0):
        return []

    temp_data = []
    for head in header:
        col = list(raw_data[head])
        temp_data.append(col)

    data = [header]
    for i in range(len(temp_data[0])):
        row = []
        for j in range(len(header)):
            row.append(temp_data[j][i])
        data.append(row)

    return data

def data_to_excel(data,out_path):
    out_path = abs_path(out_path)
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("Sheet1")
    for i in range(len(data)):
        row = data[i]
        for j in range(len(row)):
            sheet.write(i,j,row[j])

    book.save(out_path)


data = excel_to_data('excel.xlsx')
print(data)

data_to_excel(data,'output.xlsx')
data = excel_to_data('output.xlsx')
print(data)
