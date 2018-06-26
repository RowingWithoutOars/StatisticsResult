# coding: utf-8

import jieba.posseg as pseg

words = pseg.cut("我叫韩彬彬,男,1981年10月02日出生,汉族,户籍所在地昆山市玉山镇绣衣新村1幢102室,现住昆山市玉山镇富贵花园11幢204室,居民身份证32058319811002943x,联系电话13862395339。")
for word, flag in words:
    print('%s %s' % (word, flag))