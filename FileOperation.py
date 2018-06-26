# coding: utf-8
import csv

# 文件操作类
# # load nonstandard data
from typing import List, Any

# 加载信息抽取的方法 返回所有抽取到的信息list,第一个元素为笔录编号
def loadNonstandard():
    path = "/Users/usts/Desktop/biluFile/result/1/"
    csv_extract_file = csv.reader(open(path+'/all.csv', 'r'))
    extract_list: List[List[Any]] = []
    for i in csv_extract_file:
        l = []
        l.append(i[0:])
        extract_list.append(l)
    print("抽取信息的长度为：", len(extract_list))
    return extract_list

# # load standard data
def loadDict():
    path = "/Users/usts/Desktop/biluFile/dataresource/UTF8/"
    csv_file = csv.reader(open(path+'updatadata.csv', 'r'))
    list = []
    for stu in csv_file:
        l = []
        l.append(stu[0])
        l.append(stu[7])
        # l.append(stu[41])
        l.append(stu[32])
        l.append(stu[33])
        l.append(stu[34])
        l.append(stu[36])
        l.append(stu[37])
        l.append(stu[39])
        list.append(l)
    dict = {}
    for i in list:
        dict[i[0]] = i
    print("字典长度：", len(dict))
    return dict

# # load standard data
def loadContentList():
    path = "/Users/usts/Desktop/biluFile/dataresource/UTF8/"
    csv_file = csv.reader(open(path+'updatadata.csv', 'r'))
    list = []
    for stu in csv_file:
        l = []
        l.append(stu[0])
        l.append(stu[29])
        list.append(l)
    del list[0]
    return list

def loadExtractInfo():
    # # load nonstandard data
    path = "/Users/usts/Desktop/biluFile/result/2/"
    csv_extract_file = csv.reader(open(path + '/all.csv', 'r'))
    extract_list = []
    for i in csv_extract_file:
        l = []
        l.append(i[0:])
        extract_list.append(l)
    print(len(extract_list))
    del extract_list[0]
    return extract_list

if __name__ == "__main__":
    result = loadNonstandard()
    print(result[1])