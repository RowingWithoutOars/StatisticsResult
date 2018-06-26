# coding: utf-8

#从数据文件中获取对话实体

import csv

# 从数据文件中加载获得对话实体
# 返回list,第一行为有效数据，标识数据已经删除 del
def loadQAEntity():
    csv_file = csv.reader(open('dataResources/updatadata.csv', 'r'))
    list = []
    for stu in csv_file:
        l = []
        l.append(stu[29])
        list.append(l)
    print("加载实体数量：", len(list))
    del list[0]
    return list

if __name__ == "__main__":
    list = loadQAEntity()
    for i in list[0]:
        print(i)