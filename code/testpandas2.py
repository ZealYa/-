
import  pandas  as pd
import numpy as np
import time
# # pandas数据访问方法.at，.iat，.loc，.iloc和.ix。
# 1 # .loc()    # 基于标签
# 2 # .iloc()   # 基于整数
# 3 # .ix()     # 基于标签和整数

#方法二：通过指定表单名的方式来读取
def readfile(filename,sheetname):
    df=pd.read_excel(filename,sheet_name = sheetname)#可以通过sheet_name来指定读取的表单
    return df

def readOneRow(sheet,nrow):
    # 1：读取指定的单行，数据会存在列表里面
    data=sheet.ix[nrow].values#0表示第一行 这里读取数据并不包含表头，要注意哦！
    return  data

def readMoreRow(sheet,sta,end):
    # 2：读取指定的多行，数据会存在嵌套的列表里面：
    data=sheet.ix[[sta,end]].values#读取指定多行的话，就要在ix[]里面嵌套列表指定行数

def readvalue(sheet,nrow,ncol):
    # 3：读取指定行列的值：
    data=sheet.ix[nrow,ncol]#读取第一行第二列的值，这里不需要嵌套列表
    print("读取{0}行{1}列的数据：\n{0}".format(nrow,ncol,data))


def readmoreRC(sheet,row_s2e,col_s2e):
    # 4：读取指定的多行多列值：
    # row_s2e=[s,e]
    # col_s2e=[name,name,...]
    # df=pd.read_excel('test.xls')
    # data=df.ix[[1,2],['名字','地址']].values#
    # 读取第一行第二行的'名字','地址'列的值，这里需要嵌套列表
    data = sheet.ix[row_s2e,col_s2e].values
    return data

# 5：获取指定列所有的行
def readAllRowfor_ncol(sheet,col_name):
    # df=pd.read_excel('test.xls')
    # data=df.ix[:,['名字','地址']].values
    # #读所有行的title以及data列的值，这里需要嵌套列表
    # col_name = [name,name,...]
    data = sheet.ix[:,col_name].values
    return data

# 6：获取行号并打印输出
def getRowNum(df):
    # df=pd.read_excel('test.xls')
    print("输出行号列表:\n",df.index.values)
# getRowNum()

def getColumnName(sheet):
    # 7：获取列名并打印输出
    # df=pd.read_excel('test.xls')
    return sheet.columns.values


# 8：获取指定行数的值：
def getrowvalue():
    df=pd.read_excel('test.xls')#随机几行，sample(x)确定
    print("输出值:\n",df.sample(2).values)
    #这个方法类似于head()方法以及df.values方法
# getrowvalue()

# 9：获取指定列的值：
def getColumnvalue(sheet,colname):
    # df=pd.read_excel('test.xls')
    return sheet[colname].values
    # print("输出值\n",df['名字'].values)
# getColumnvalue()

def finddata(demo_df,data):
    # 读取数据所在的行和列
    # demo_df=pd.read_excel(r'1.xlsx')  ##文件路径
    for indexs in demo_df.index:
        # for i in range(len(demo_df.loc[indexs].values)):
            if (demo_df.loc[indexs].values[3] == data):
                print('行数：',indexs+2, '列数：',3+1)
                # print(demo_df.loc[indexs].values[i])
                print(demo_df.ix[indexs].values)
    print(type(demo_df.index), len(demo_df.index)+1)
    # print('共{}行'.format(indexs))

def selectallNo(xuhao):
    return set(xuhao)

def all_np(arr):#获取所有元素的出现次数
    arr = np.array(arr)
    key = np.unique(arr)
    result = {}
    for k in key:
        mask = (arr == k)
        arr_new = arr[mask]
        v = arr_new.size
        result[k] = v
    return key,result

def getSta_End(len_dict,key,n):
    # 取一个表里的不同序号点的起始值
    if n==0:
        spoint = 0
        epoint = len_dict[key[n]]-1
        Offset_step = 0
        return spoint,epoint,Offset_step
    else:
        spoint = 0
        epoint = 0
        Offset_step = 0
        for index in range(0,n):
            spoint = len_dict[key[index]] + spoint
            if index == n-1:
                Offset_step = spoint
                epoint = spoint+len_dict[key[n]]-1
        return spoint,epoint,Offset_step

def getPoinData(sheet,srow,erow):
    return  sheet.ix[srow:erow,:]


def process_3k_300excel():
    all_sheet = readfile('test300row.xls','Sheet1')
    # print()

def sameXuhao_disaAttr(it_sheet,nstart,nend,clun):
    # 统计不同类别
    # 第二列是类别
    keys, isaAttr = all_np(it_sheet.ix[nstart:nend, clun].values)
    return keys,isaAttr

def disAttr_stat_end(alldict,key,nstart,n):
    if n==0:
        spoint = nstart
        epoint = alldict[key[n]]-1
        # Offset_step = 0
        return spoint,epoint#,Offset_step
    else:
        spoint = nstart
        epoint = 0
        #Offset_step = 0
        for index in range(0,n):
            spoint = alldict[key[index]] + spoint
            if index == n-1:
                #Offset_step  = alldict[key[n]]
                epoint = spoint+alldict[key[n]]-1
        return spoint,epoint#,Offset_step

def get_attr_ix_iy(attribute_values,flag_attr_key):
    # flag_attr_key[0] 为attribute_values里的key值
    # 传入直接flag_attr_key，取值第几个就第几个
    attr_ix_iy=np.where(attribute_values == flag_attr_key)
    return attr_ix_iy[0]
    # attr_ix_iy[0][n]为取到下标
    # print(attr_ix_iy[0])
    # print(attr_ix_iy[0][1])

# def get_sheet_sameAttr_ixiy(df,srow,erow,):
#     找出一个类别的比如 小区，学习
#     flag_attr_key,flag_attr=sameXuhao_disaAttr(df,srow,erow)

    # pass



def maintest():
    df = readfile('15.xlsx', 'Sheet1')
    # finddata(df,'天大六村')
    # 第一列是取点不同序号
    keys,xuhao_one = all_np(df.ix[:,0].values)
    print(keys)
    print('>->-'*16)
    print(xuhao_one)
    print('>->-'*16)
    # print(xuhao_one[keys[0]])
    # srow = xuhao_one[keys[1]]
    # erow = xuhao_one[keys[1]]
    select_n = 2
    srow,erow,Offset_step=getSta_End(xuhao_one,keys,select_n)
    print('选择的序号',keys[select_n],'点起止值:',srow,erow,'<',erow-srow)
    print('选择的起止值name:',df.ix[srow,3],df.ix[erow,3])
    # print(getPoinData(df,srow,erow))
    # print(len(df.ix[srow:erow,'属性'].values))
    # print(df.ix[srow:erow,'属性'].values)
    attribute_values = df.ix[srow:erow, '属性'].values
    # 2019.7.9 11:24am

    print('attribute_values:>>type:>',type(attribute_values))
    flag_attr_key,flag_attr=sameXuhao_disaAttr(df,srow,erow)
    print(flag_attr_key)
    print('>->-' * 16)
    print(flag_attr)
    print('>->-' * 16)
    # print(attribute_values)
    # attr_ix_iy=np.where(attribute_values == flag_attr_key[0])
    print(flag_attr_key[6])
    ixiy=get_attr_ix_iy(attribute_values, flag_attr_key[6])
    # print(type(ixiy),ixiy)
    # print(Offset_step,xuhao_one[keys[select_n-1]])
    ixiy_add = np.add(ixiy,Offset_step)
    print(ixiy_add)
    # result = [x + 1 for x in first_list]
    print(df.ix[ixiy_add[0]])
    print(df.ix[ixiy_add[-1]])
    # print(df.ix[ixiy[13]])
    print('值求和：',sum(flag_attr.values()))
    # print(attr_ix_iy[0][1])


# if __name__ == '__main__':
def runit():
    # cov2dict()
    # process_3k_300excel()
    starttime = time.clock()
    # 当中是你的程序

    maintest()
    # run结束
    elapsed = (time.clock() - starttime)
    print("Time used:{} s".format(elapsed))






