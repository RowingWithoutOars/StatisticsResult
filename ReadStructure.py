# coding: utf-8

import csv
import pandas as pd

# 需要获取的属性：
# 笔录编号 ID 1
# 笔录制作单位 ADDRESS 8
# 笔录关键字 GJZKEYWORD 42
# 报案人姓名 BAR_XM 33
# 报案人性别 BAR_XB 34
# 报案人身份证号 '''||PG.BAR_SFZHM 35
# 报案人电话  '''||PG.BAR_DH 37
# 报案人户籍所在地 BAR_HJD 38
# 报案人现住址 BAR_XZDZ 40
# 笔录中出现的时间
# 笔录中出现的地点信息
# 笔录中出现的人物
def isRight(str1, str2,i):
    if len(str1) == 0:
        return False
    if len(str2) == 0:
        return False
    if str1 in str2:
        if len(str1)/len(str2) > i or len(str1)/len(str2) == i:
            return True
        else:
            return False
    else:
        return False


# # load standard data
csv_file = csv.reader(open('dataResources/updatadata.csv', 'r'))
list = []
for stu in csv_file:
    l = []
    l.append(stu[0])
    l.append(stu[7])
    l.append(stu[41])
    l.append(stu[32])
    l.append(stu[33])
    l.append(stu[34])
    l.append(stu[36])
    l.append(stu[37])
    l.append(stu[39])
    list.append(l)
print(len(list))

# # load nonstandard data
path = "/Users/usts/Desktop/biluFile/result/2/"
csv_extract_file = csv.reader(open(path+'/all.csv', 'r'))
extract_list = []
for i in csv_extract_file:
    l = []
    l.append(i[0:])
    extract_list.append(l)
print(len(extract_list))

# Setting up a dictionary according to the standrad
dict = {}
for i in list:
    dict[i[0]] = i

# # Defining the correct number of variables
addressCount = 0
dicaddresscount = 0
noAddressCount = 0

keyWordCount = 0

xmCount = 0
noXmCount = 0
dicXmCount = 0

xbCount = 0
noXbCount = 0
dicXbCount = 0

sfzhmCount = 0
noSfzhmCount = 0
dicSfzhmCount = 0
errsfzh = 0

dhCount = 0
noDhCount = 0
dicDhCount = 0

hjdCount = 0
nohjdCount = 0
dicHjdCount = 0

xzdzCount = 0
noXzdzCount = 0
dicXzdzCount = 0

allCount = 0
allRightCount = 0
# ex_list = extract_list[1]
# ex_index = ex_list[0][0]
# dict_list = dict[ex_index]

# for i in ex_list[0]:
#     # for j in i:
#     print(i)
#
# print("============================")
# for i in dict_list:
#     print(i)
xberr = 0
runcount = 0
m = 0
for ex_list in extract_list:
    # ex_list = extract_list[i]
    try:

        allRight = 1
        rightruncount = 0
        ex_index = ex_list[0][0]
        dict_list = dict[ex_index]

        if ex_list[0][1] == dict_list[1] or dict_list[1] in ex_list[0][1]:
            addressCount = addressCount+1
            rightruncount += 1
        else:
            if len(ex_list[0][1]) == 0:
                noAddressCount += 1
            if len(dict_list[1]) == 0:
                dicaddresscount += 1
            allRight = 0

        if ex_list[0][2] == dict_list[2]:
            keyWordCount += 1
        # else:
            # allRight = 0

        if ex_list[0][3] == dict_list[3]:
            xmCount += 1
            rightruncount += 1
        else:
            if len(ex_list[0][3]) == 0:
                noXmCount += 1
            if len(dict_list[3]) == 0:
                dicXmCount += 1
            allRight = 0

        if ex_list[0][4] == dict_list[4]:
            xbCount += 1
            rightruncount += 1
        else:
            if len(ex_list[0][4]) == 0:
                noXbCount += 1
            if len(dict_list[4]) == 0:
                dicXbCount += 1
            allRight = 0

        # if ex_list[0][5] == dict_list[5]:
        #     sfzhmCount += 1
        #     rightruncount += 1
        # else:
        #     if len(ex_list[0][5]) == 0:
        #         noSfzhmCount += 1
        #     if len(dict_list[5]) == 0:
        #         dicSfzhmCount += 1
        #     allRight = 0
        if not len(ex_list[0][5]) == 0:
            if ex_list[0][5] == dict_list[5]:
                sfzhmCount += 1
                rightruncount += 1
            else:
                errsfzh += 1
        else:
            noSfzhmCount += 1

        if ex_list[0][6][0:11] if(len(ex_list[0][6]) > 11) else ex_list[0][6] == dict_list[6]:
            dhCount += 1
            rightruncount += 1
        else:
            if len(ex_list[0][6]) == 0:
                noDhCount += 1
            if len(dict_list[6]) == 0:
                dicDhCount += 1
            allRight = 0

        # if ex_list[0][7] == dict_list[7]:
        #     hjdCount += 1
        # else:
        #     allRight = 0
        if isRight(ex_list[0][7], dict_list[7], 0.1):
            hjdCount += 1
            rightruncount += 1
        else:
            if len(ex_list[0][7]) == 0:
                nohjdCount += 1
            if len(dict_list[7]) == 0:
                dicHjdCount += 1
            allRight = 0
        # if ex_list[0][8] == dict_list[8]:
        #     xzdzCount += 1
        # else:
        #     allRight = 0
        if isRight(ex_list[0][8], dict_list[8], 0.1):
            xzdzCount += 1
            rightruncount += 1
        else:
            if len(ex_list[0][8]) == 0:
                noXzdzCount += 1
            if len(dict_list[8]) == 0:
                dicXzdzCount += 1
            allRight = 0

        if allRight == 1:
            allCount += 1
        if rightruncount == 7:
            allRightCount += 1
        m += 1
        if m > runcount*len(extract_list)/100:
            print(runcount)
            runcount += 1
    except KeyError:
        print("KeyError")
print("录制单位正确率：", addressCount, noAddressCount, dicaddresscount, addressCount/len(extract_list))
print("关键字正确率：", keyWordCount, keyWordCount/len(extract_list))
print("姓名正确率：", xmCount, noXmCount, dicXmCount, xmCount/len(extract_list))
print("性别正确率：", xbCount, noXbCount, dicXbCount, xbCount/len(extract_list))
print("身份证号码正确率：", sfzhmCount, noSfzhmCount, dicSfzhmCount, errsfzh, sfzhmCount/len(extract_list))
print("电话正确率：", dhCount, noDhCount, dicDhCount, dhCount/len(extract_list))
print("户籍地正确率：", hjdCount, nohjdCount, dicHjdCount, hjdCount/len(extract_list))
print("现居地址正确率：", xzdzCount, noXzdzCount, dicXzdzCount, xzdzCount/len(extract_list))
print("总正确率：", allCount, allRightCount, allCount/len(extract_list))
print(len(extract_list))
print(len(dict))
print(allRightCount)