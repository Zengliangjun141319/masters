# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     StringOrders.py
   Description :   把字符串内容随机打乱再输出
   Author :        曾良均
   QQ:             277099728
   Date：          10/21/2021 12:24 PM
-------------------------------------------------
   Change Activity:
                   10/21/2021:
-------------------------------------------------
"""
__author__ = 'ljzeng'


import random
from random import shuffle

def randomize(str1):
    l = len(str1)
    loc = []
    n = 0
    while True:    # 用于生成随机位置
        k = random.randint(0, l-1)
        if k not in loc:
            loc += [k]
            n += 1
        if n == l:
            break

    out = []
    for s in loc:
        out.append(str1[s:s+1])

    out = ''.join(out)
    return out


if __name__ == '__main__':
    while True:
        strings = input('Enter the words: ')
        if strings == '':     # 如果不输入内容，直接回车，则退出
            break
        strs = strings.split(' ')
        oo = []
        for s in strs:
            # 方法一：自定义函数
            # oo.append(randomize(s))

            # 方法二： 引用Random的shuffle方法
            s = list(s)    # 把字符串转为List
            shuffle(s)        # 随机打乱List中元素位置
            oo.append(''.join(s))   # 把打乱后的元素合并为字符串，并追加到一起


        print(' '.join(oo))