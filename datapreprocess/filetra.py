#  coding: utf-8

# File traversal
import fasttext
import os

def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    dirlist = []
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        dirlist.append(child)
    return dirlist

def divfile(dirlist):
    train_list = []
    test_list = []
    for dir in dirlist:
        if 'test' in dir:
            test_list.append(dir)
        elif 'train' in dir:
            train_list.append(dir)
        else:
            print(dir)
    return train_list, test_list

if __name__ == '__main__':
    basePath = '../resources/'  # linux 下资源目录
    modelPath = '../model/'
    # basePath = ''../resource/biluFile/fasttext/'  #windows 下资源目录
    dirlist = eachFile(basePath)    # 获取所有文件
    train_list, test_list = divfile(dirlist)    # 分开测试文件和训练文件
    for train in train_list:
        testfile = train.replace("train", "test")   # 获取到test文件路径
        modelfilename = train.replace("csv", "model")
        classifier = fasttext.supervised(basePath+train, modelPath+modelfilename, '_label_')
        result = classifier.test(basePath+testfile)
        print(train, result.precision, result.recall)
# import fasttext
#
# classifier = fasttext.supervised('../resources/EJWP_train_list.csv','../model/ejwp.model','_label_')
# result = classifier.test('../resources/EJWP_test_list.csv')
#
# print(result.precision)
# print(result.recall)
