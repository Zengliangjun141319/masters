# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     requestNumber.py
   Description :   不用For、While循环实现求水仙花数
   Author :        曾良均
   QQ:             277099728
   Date：          9/16/2021 9:31 AM
-------------------------------------------------
   Change Activity:
                   9/16/2021:
-------------------------------------------------
"""
__author__ = 'ljzeng'

n = int(input("请输入数字位数："))
listNum = []
def sxh(x):
    num = sum(map(lambda i:i**n, list(map(int,str(x)))))
    if num == x:
        listNum.append(str(x))
ll = list(map(lambda x: sxh(x), range(10**(n-1),10**n)))
print("\n".join(listNum))