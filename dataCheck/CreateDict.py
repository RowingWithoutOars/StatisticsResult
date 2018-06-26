# coding: utf-8
from typing import Type, Dict, Any
import FileOperation as fo


# 0 表示长度为0，1 表示存在与对话中，2 表示长度不为0且不存在与对话中

dict = fo.loadDict()
print(len(dict))
# 加载抽取信息方法，获得所有抽取到的信息
content_list = fo.loadContentList()
i = content_list[1][0]
# print(dict[i])
# 构建地址字典
def buildAddressDict():
    zoneCount = 0
    isIn = 0
    notIn = 0
    addressDict: Dict[Any, Type[list]] = {}
    for content in content_list:
        index = content[0]
        dict_list = dict[index]
        tmp_list = [dict_list[1]]
        if len(dict_list[1]) == 0:
            tmp_list.append(0)
            zoneCount += 1
        else:
            if dict_list[1] in content[1]:
                tmp_list.append(1)
                isIn += 1
            else:
                tmp_list.append(2)
                notIn += 1
        addressDict[index] = tmp_list
    print(zoneCount, isIn, notIn)
    return addressDict

# 构建姓名字典
def buildXmDict():
    zoneCount = 0
    isIn = 0
    notIn = 0
    xmDict: Dict[Any, Type[list]] = {}
    for content in content_list:
        index = content[0]
        dict_list = dict[index]
        tmp_list = [dict_list[2]]
        if len(dict_list[2]) == 0:
            tmp_list.append(0)
            zoneCount += 1
        else:
            if dict_list[2] in content[1]:
                tmp_list.append(1)
                isIn += 1
            else:
                tmp_list.append(2)
                notIn += 1
        xmDict[index] = tmp_list
    print(zoneCount, isIn, notIn)
    return xmDict

# 构建性别字典
def buildXbDict():
    zoneCount = 0
    isIn = 0
    notIn = 0
    xbDict: Dict[Any, Type[list]] = {}
    for content in content_list:
        index = content[0]
        dict_list = dict[index]
        tmp_list = [dict_list[3]]
        if len(dict_list[3]) == 0:
            tmp_list.append(0)
            zoneCount += 1
        else:
            if dict_list[3] in content[1]:
                tmp_list.append(1)
                isIn += 1
            else:
                tmp_list.append(2)
                notIn += 1
        xbDict[index] = tmp_list
    print(zoneCount, isIn, notIn)
    return xbDict

# 构建身份证号字典
def buildSfzhDict():
    zoneCount = 0
    isIn = 0
    notIn = 0
    SfzhDict: Dict[Any, Type[list]] = {}
    for content in content_list:
        index = content[0]
        dict_list = dict[index]
        tmp_list = [dict_list[4]]
        if len(dict_list[4]) == 0:
            tmp_list.append(0)
            zoneCount += 1
        else:
            if dict_list[4] in content[1]:
                tmp_list.append(1)
                isIn += 1
            else:
                tmp_list.append(2)
                notIn += 1
        SfzhDict[index] = tmp_list
    print(zoneCount, isIn, notIn)
    return SfzhDict

# 构建电话字典
def buildDhDict():
    zoneCount = 0
    isIn = 0
    notIn = 0
    dhDict: Dict[Any, Type[list]] = {}
    for content in content_list:
        index = content[0]
        dict_list = dict[index]
        tmp_list = [dict_list[5]]
        if len(dict_list[5]) == 0:
            tmp_list.append(0)
            zoneCount += 1
        else:
            if dict_list[5] in content[1]:
                tmp_list.append(1)
                isIn += 1
            else:
                tmp_list.append(2)
                notIn += 1
        dhDict[index] = tmp_list
    print(zoneCount, isIn, notIn)
    return dhDict

# 构建户籍地字典
def buildHjdDict():
    zoneCount = 0
    isIn = 0
    notIn = 0
    HjdDict: Dict[Any, Type[list]] = {}
    for content in content_list:
        index = content[0]
        dict_list = dict[index]
        tmp_list = [dict_list[6]]
        if len(dict_list[6]) == 0:
            tmp_list.append(0)
            zoneCount += 1
        else:
            if dict_list[6] in content[1]:
                tmp_list.append(1)
                isIn += 1
            else:
                tmp_list.append(2)
                notIn += 1
        HjdDict[index] = tmp_list
    print(zoneCount, isIn, notIn)
    return HjdDict

# 构建现地址字典
def buildXzzDict():
    zoneCount = 0
    isIn = 0
    notIn = 0
    xzzDict: Dict[Any, Type[list]] = {}
    for content in content_list:
        index = content[0]
        dict_list = dict[index]
        tmp_list = [dict_list[7]]
        if len(dict_list[7]) == 0:
            tmp_list.append(0)
            zoneCount += 1
        else:
            if dict_list[7] in content[1]:
                tmp_list.append(1)
                isIn += 1
            else:
                tmp_list.append(2)
                notIn += 1
        xzzDict[index] = tmp_list
    print(zoneCount, isIn, notIn)
    return xzzDict

if __name__ == "__main__":
    buildAddressDict()
    # buildXmDict()
    # buildXbDict()
    # buildSfzhDict()
    # buildDhDict()
    # buildHjdDict()
    # buildXzzDict()