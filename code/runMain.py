#! /usr/bin/env python  
# from testpandas2 import *
from string_similarity import *
# import time
from write2EXCEL import *
import sys

if __name__ == '__main__':
    # testpandas2.runit()
    # string_similarity.testsimi()

    starttime = time.clock()
    # 当中是你的程序
    # excel_name = your_excel_Name#你需要处理的文件名字
    excel_name = sys.argv[1] #外部传入文件名，直接运行需要注释掉
    # cmd运行： python runMain.py 15.xlsx > 15_report.txt
    # 运行runMain.py 传入处理文件名15.xlsx，日志结果保存到15_report.txt中
    # linux 中 如需运行： 以下demo命令
    # nohup python -u runMain.py 22.xlsx > report_22H.log 2>&1 &


    df, highlightRows, excelName = get_sheet_sameAttr_ixiy(excel_name)
    highlight_sheet_rows(df,highlightRows,excelName)
    # test_highlight()
    # testsimi()

    # run结束
    elapsed = (time.clock() - starttime)
    print('#*'*20)
    print("<!>Time used<!>:{} s".format(elapsed))


