#   coding: utf-8
#   将csv文件转化为xlsx文件

import pandas as pd

def xlsx_to_csv_pd():
    path = "/Users/usts/Desktop/biluFile/result/2/"
    for i in range(1, 6):
        data_xls = pd.read_excel(path + str(i)+".xls", index_col=0)
        data_xls.to_csv(path+str(i)+'.csv', encoding='utf-8')


if __name__ == '__main__':
    xlsx_to_csv_pd()