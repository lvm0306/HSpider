import xlsxwriter as xw

date = [[1, 20, '可乐'], [2, 40, '雪碧']]


def run():
    wb = xw.Workbook('testexcel.xlsx')
    sheet1 = wb.add_worksheet('to1')
    sheet1.activate()
    title = ['第一行', '第二行', '第三行']
    sheet1.write_row('A1', title)
    sheet1.write_row('A2', date[0])
    sheet1.write_row('A3', date[1])
    wb.close()
    pass


if __name__ == '__main__':
    run()
    pass
