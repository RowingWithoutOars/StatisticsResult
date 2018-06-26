# coding: utf-8

import FileOperation as fo

# 源数据校验方法

# 查看content中是否包含所有完全匹配字段
# 所有能够抽取到的字段都应该在对话中含有
# 关于地址方面 词袋模型 词频相似度算法 ？？
# 源数据集最好使用dict
# content_list = []
dict = fo.loadDict()
print(len(dict))
# 加载抽取信息方法，获得所有抽取到的信息
content_list = fo.loadContentList()
print(len(content_list))
print(content_list[1])
# 通过 extarct_list 来作为循环体，字典校验
address = 0
addressBlank = 0
addressNoin = 0

xm = 0
xmBlank = 0
xmNoin = 0

xb = 0
xbBlank = 0
xbNoin = 0

dh = 0
dhBlank = 0
dhNoin = 0

sfzh = 0
sfzhBlank = 0
sfzhNoin = 0

hjd = 0
hjdBlank = 0
hjdNoin = 0

xdz = 0
xdzBlank = 0
xdzNoin = 0

# print(content_list[1][0])
# print(dict[content_list[1][0]])
for extarct in content_list:
    try:
        d = dict[extarct[0]]

        if len(d[1]) != 0:
            if d[1] in extarct[1]:
                address += 1
            else:
                addressNoin += 1
        else:
            addressBlank += 1

        if len(d[3]) != 0:
            if d[3] in extarct[1]:
                xm += 1
            else:
                xmNoin += 1
        else:
            xmBlank += 1
        if len(d[4]) != 0:
            if d[4] in extarct[1]:
                xb += 1
            else:
                xbNoin += 1
        else:
            xbBlank += 1
        if len(d[5]) != 0:
            if d[5] in extarct[1]:
                sfzh += 1
            else:
                sfzhNoin += 1
        else:
            sfzhBlank += 1

        if len(d[6]) != 0:
            if d[6] in extarct[1]:
                dh += 1
            else:
                dhNoin += 1
        else:
            dhBlank += 1

        if len(d[7]) != 0:
            if d[7] in extarct[1]:
                hjd += 1
            else:
                hjdNoin += 1
        else:
            hjdBlank += 1
        if len(d[8]) != 0:
            if d[8] in extarct[1]:
                xdz += 1
            else:
                xdzNoin += 1
        else:
            xdzBlank += 1
    except TypeError:
        print("TypeError")
    except IndexError:
        pass
print("录制单位", address, addressBlank, addressNoin)
print("姓名", xm, xmBlank, xmNoin)
print("性别", xb, xbBlank, xbNoin)
print("电话", dh, dhBlank, dhNoin)
print("身份证号", sfzh, sfzhBlank, sfzhNoin)
print("户籍所在地", hjd, hjdBlank, hjdNoin)
print("现住址", xdz, xdzBlank, xdzNoin)
