# coding: utf-8

import re


# 通过正则表达式实现信息提取的类

# 电话号码提取
def extractTeleNumber(value):
    pattern = "((17[0-9])|(13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}"
    # 需要做非空判断，
    # print(re.search(pattern, value).group())
    result = re.search(pattern, value)
    if result:
        return result.group()
    else:
        return ""


# 身份证号码提取
def extractIdNumber(value):
    pattern = "\\d{6}((19|20)\\d{2})((0[0-9])|(1[0-2]))(((0|1|2)[0-9])|(3[0,1]))\\d{3}[xX\\d]"
    # 需要做非空判断，
    # print(re.search(pattern, value).group())
    result = re.search(pattern, value)
    if result:
        return result.group()
    else:
        return ""


# 测试函数
if __name__ == "__main__":
    print(extractTeleNumber("联系电话15895631111"))
    print(extractIdNumber("居民身份证32058319930301042X"))
