# -*- coding:utf-8 -*-

import xlrd

def open_xls(file='IATC_Para.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as msg:
        print(msg)

def excel_table_cell(file="IATC_Para.xls", colindex=0, byIndex=0):
    data = open_xls(file)
    table = data.sheets()[byIndex]
    nrows = table.nrows    # 行数
    nclo = table.ncols      # 列数
    coldatas = table.row_values(colindex)   # 某一行数据
    list = []

    print("第1组数据： \n")
    for i in coldatas:
        print(i)

if __name__ == '__main__':
    excel_table_cell(colindex=2)