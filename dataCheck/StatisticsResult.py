# coding:utf-8

import FileOperation
import dataCheck.CreateDict as createDict

# [[
# '000636dc-b968-4540-a28e-5944f24d1d22',
# '城中派出所',
# '积分兑换#对方#积分#信用卡#电话#',
# '王玲',
# '女',
# '34082319800317582X',
# '15995617028.0',
# '安徽省安庆市枞阳县',
# '江苏省昆山市',
# '1980年03月17日,02号,2017年6月12日,', '', ''
# ]]

extract_list = FileOperation.loadExtractInfo()
addressDict = createDict.buildAddressDict()
xbDict = createDict.buildXbDict()
sfzhDict = createDict.buildSfzhDict()
dhDict = createDict.buildDhDict()
xmDict = createDict.buildXmDict()

if __name__ == "__main__":
    zone = 0
    Tright = 0
    Terror = 0
    Fright = 0
    Ferror = 0
    count = 0
    for i in extract_list:
        try:
            index = i[0][0]
            address = xmDict[index]
            extract_address = i[0][3]
            if not len(extract_address) == 0:
                if not extract_address.find(address[0]) == -1:
                    Tright += 1
                else:
                    if address[1] == 2:
                        Fright += 1
                    else:
                        Terror += 1
            else:
                zone += 1
                if address[1] == "0":
                    Fright += 1
                else:
                    Ferror += 1
        except KeyError:
            count += 1
            pass
    print(zone, Tright, Terror, Fright, Ferror, count)
