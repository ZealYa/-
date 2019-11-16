
import difflib
from testpandas2 import *
import math,cmath
# import sys
def string_similar(s1, s2):
    if isinstance(s1,int) or isinstance(s2,int):
        print(s1,s2)
        s11 = str(s1)
        s22 = str(s2)
    else:
        s11 = s1
        s22 = s2
    return difflib.SequenceMatcher(None, s11, s22).quick_ratio()


def testsimi():#测试例子
    print('-*-' * 16)
    print (string_similar('爱尔眼科沪滨第一医院', '沪滨爱尔眼科第二医院'))
    print (string_similar('安定区妇幼保健站', '定西市安定区妇幼保健站'))
    print (string_similar('成都第一人民医院', '成都第二人民医院'))
    print(string_similar('首都医科大学-博源楼','首都医科大学博雅楼'))

def isSameLocation(df,ii,jj):
    # issame = 1
    # 在经线上，纬度每差1度, 实地距离大约为111千米；
    # 在纬线上，经度每差1度, 实际距离为111×cosθ千米。
    # （其中θ表示该纬线的纬度.在不同纬线上, 经度每差1度的实际距离是不相等的）。
    standDistance = 111000#
    issame = 0
    # df.ix[ii,4],  df.ix[jj,5]
    #   纬度，         经度
    standDistance_cos = 111000*math.cos(df.ix[ii,4])
    distance2location_w = math.pow((df.ix[ii,4]-df.ix[jj,4])*standDistance,2)
    distance2location_j = math.pow((df.ix[ii,5]-df.ix[jj,5])*standDistance_cos,2)
    distance2location = math.sqrt(distance2location_w+distance2location_j)
    if distance2location > 1000:#大于1.5km的位置就判为两个地方
        issame=0
    else:
        print('相距：',distance2location, 'm')
        # if string_similar(df.ix[ii,6],df.ix[jj,6])>0.8:
        issame = 1
    return issame


# 读excel处理
def get_sheet_sameAttr_ixiy(excelName):
    # 找出一个类别的比如 小区，学习
    # excelPath = 'C://Users//ZealYa//Desktop//isu_data_process//'
    # excelName1 = '15'
    # excelName1=sys.argv[1]
    excelName2 = '.xlsx'
    # excelName = excelName1#+excelName2
    excelSaveName = excelName+'_highLight'+excelName2
    df = readfile(excelName, 'Sheet1')
    # finddata(df,'天大六村')
    # 第一列是取点不同序号
    keys, xuhao_one = all_np(df['序号'].values)
    print(keys)
    print('>->->' * 16)
    print(xuhao_one)
    print('>->->' * 16)
    highlightRows=[]

    # select_n = 0# 对应无地点序号0开始
    # arrytest = get_sheet_sameAttr_ixiy_son(df,xuhao_one, keys,select_n)
    # highlightRows.extend(arrytest)

    for select_n in range(0,len(keys)):
        arrytest = get_sheet_sameAttr_ixiy_son(df, xuhao_one, keys, select_n)
        highlightRows.extend(arrytest)

    return df,highlightRows,excelSaveName

def get_sheet_sameAttr_ixiy_son(df,xuhao_one, keys, select_n):
    # select_n = 2
    srow, erow, Offset_step = getSta_End(xuhao_one, keys, select_n)
    print('选择的序号', keys[select_n], '点起止值:', srow,'<->', erow, ':', erow - srow)
    print('选择的起止值name:', df.ix[srow, 3], df.ix[erow, 3])
    # print(getPoinData(df,srow,erow))
    # print(len(df.ix[srow:erow,'属性'].values))
    # print(df.ix[srow:erow, '属性'].values)
    attribute_values = df.ix[srow:erow, '属性'].values
    # 2019.7.9 11:24am

    # print('attribute_values:>>type:>', type(attribute_values))
    flag_attr_key, flag_attr = sameXuhao_disaAttr(df, srow, erow,1)#1为第1列
    # print(flag_attr_key)
    print('>->-' * 16)
    print(flag_attr)
    print('>->-' * 16)
    tempArry = []
    for itt in range(0,len(flag_attr_key)):
        n_key = itt#d对应于地点的属性比如'中学' '公交站' '公园'
        # print(flag_attr_key[6])
        ixiy = get_attr_ix_iy(attribute_values, flag_attr_key[n_key])
        # print(type(ixiy),ixiy)
        # print(Offset_step,xuhao_one[keys[select_n-1]])
        ixiy_add = np.add(ixiy, Offset_step)
        # print(ixiy_add)   #下标值

        #2019.07.10 9:00am 名字相似度计算整合
        similar_sameAtt = []
        ixiy_add2 = ixiy_add
        for ii in ixiy_add:
            if ii not in similar_sameAtt:
                for jj in ixiy_add2:
                    if (jj not in similar_sameAtt) and (ii !=jj):
                        si_temp = string_similar(df.ix[ii,3],df.ix[jj,3])
                        if si_temp > 0.9:
                            if isSameLocation(df,ii,jj):
                                similar_sameAtt.append(jj)
                                print('相似的两个为：',ii,df.ix[ii,3],jj,df.ix[jj,3])
            # print(similar_sameAtt)

        #
        print('去除序号{0}中-<{1}>的相似度较高的：'.format(keys[select_n],flag_attr_key[n_key]))
        print(similar_sameAtt)
        tempArry.extend(similar_sameAtt)
        # highlightRows = highlightRows + similar_sameAtt
        print('共有：',len(similar_sameAtt),'个')
        print(df.ix[similar_sameAtt,3])
        print('\n')
    print('·>·<·'*24)
    print('\n')
    return tempArry




















