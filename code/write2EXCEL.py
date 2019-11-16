
# 删除，高亮，写入excel

from testpandas2 import *


def drop_sheet_rows(Dataframe,dropRows):
    dropdata = Dataframe.drop(index=dropRows)
    return dropdata

def highlight_sheet_rows_test(data,highlightRows,saveName):
    # data = readfile('test300row.xls', 'Sheet1')
    # dropRows = [1, 10, 20]
    writer = pd.ExcelWriter(saveName, engine='xlsxwriter')
    # pd.core.format.header_style = None
    data.to_excel(writer, sheet_name='clearData')  # , index=False)
    workbook = writer.book
    worksheet = writer.sheets['clearData']
    # formatdict = {'font_name': 'Calibri', 'font_size': 10, 'font_color':'black'}
    formatdict = {'font_color': 'black'}
    # font_fmt = workbook.add_format(formatdict)
    # worksheet.set_column('A:A', None, font_fmt)
    zebra = workbook.add_format(formatdict)
    zebra.set_bg_color('yellow')
    ll = len(highlightRows)
    for index in range(0,ll-1):  # range(1,6,2)#1->6 步长为2
        H_row = highlightRows[index]-index
        worksheet.set_row(H_row, None, zebra)
    # worksheet.set_row(dropRows, None, zebra)
    writer.save()
    return 0


def highlight_sheet_rows(data,highlightRows,saveName):
    # filePath = 'C://Users//ZealYa//Desktop//isu_data_process//highlight//'#highlightData//'
    # filePath_Name = filePath + saveName
    writer = pd.ExcelWriter(saveName, engine='xlsxwriter')
    data.to_excel(writer, sheet_name='highlightData')  # , index=False)
    workbook = writer.book
    worksheet = writer.sheets['highlightData']
    formatdict = {'font_color': 'black'}
    zebra = workbook.add_format(formatdict)
    zebra.set_bg_color('yellow')
    # ll = len(highlightRows)
    for index in highlightRows: #range(0,ll-1):  # range(1,6,2)#1->6 步长为2
        # H_row = highlightRows[index]
        worksheet.set_row(index+1, None, zebra)
    # worksheet.set_row(dropRows, None, zebra)
    writer.save()
    return 0

# filePath = 'C://Users//ZealYa//Desktop//isu_data_process//highlight//'
#
# highlightrows = [2,11,21,291]
# nan_excle = readfile(filePath+'test300row.xls','Sheet1')
# highlight_sheet_rows(nan_excle,highlightrows,'test300row_h.xlsx')

#######################################
def test_highlight():
    # dropRows = [1,10,20,290]
    highlightrows = [2,11,21,291]
    nan_excle = readfile('test300row.xls','Sheet1')
    # nan_excle.to_excel('test300row.xls')
    # dropdata = drop_sheet_rows(nan_excle,dropRows)
    highlight_sheet_rows(nan_excle,highlightrows,'test300row-h.xlsx')
    # print('删除：')
    # print(nan_excle.ix[dropRows])
    # print('高亮：')
    print(nan_excle.ix[highlightrows])
