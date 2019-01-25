# coding: utf-8

#将文本转化为fasttext的输入文本
import csv
import jieba
import Tools.FileIO as fileIO
import Tools.Utils as Utils

basePath = "D:/pizhou/pyCharmWorkSpaces/Statistics/resource/biluFile/biluFile/"
csv_file = csv.reader(open(basePath+'dataresource/GB2312/updatadata.csv', 'r'))

# 将文件转化成表
entryList = []
for entry in csv_file:
     #29 是笔录内容
    entryList.append(entry)

# 按照属性，将其写入到文本中
# fasttext 的 文本段需要做分词处理content _label_default label
defaultLabel = entryList[0]
del entryList[0]
# for entry in entryList:
#     content = entry[29]  # 获取笔录内容
#     words = jieba.cut(content)  # 结巴分词
#     seg = ' '.join(words)
#     seg = seg + '   _label_'  # 在后面加类别尾缀
#     for index in range(len(defaultLabel)):
#         label = defaultLabel[index]
#         fileIO.writeFile(seg+label, label+'.csv')
# keylist = [40, 41, 42, 43, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
keylist = [ 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
for index in keylist:
    classifierList = []
    print(defaultLabel[index], index)
    label = defaultLabel[index]
    for entry in entryList:
        label = entry[index]
        content = entry[29]
        content = str(content).replace('\n','')
        words = jieba.cut(content)  # 结巴分词
        seg = ' '.join(words)
        seg = seg + '   _label_'  # 在后面加类别尾缀
        seg = seg + label
        classifierList.append(seg) # 将一行加入到list中便于后续打乱和切分
    train_list, test_list = Utils.split(classifierList, shuffle=True, ratio=0.8)
    fileIO.writeFileForList(train_list, defaultLabel[index]+"_train_list.csv")
    fileIO.writeFileForList(test_list,  defaultLabel[index]+"_test_list.csv")
    print(defaultLabel[index]+' is done!')
print('all done')
