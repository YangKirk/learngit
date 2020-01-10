# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ysf_xyx
   Description :
   Author :       Kirk
   date：          2020/1/7
-------------------------------------------------
   Change Activity:
                   2020/1/7:
-------------------------------------------------
"""
__author__ = 'Kirk'
"""
30 个人在一条船上，超载，需要 15 人下船。

于是人们排成一队，排队的位置即为他们的编号。

报数，从 1 开始，数到 9 的人下船。

如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
"""
people = {}
for x in range(1, 31):
    people[x] = 1  # 遍历总共30人都是1，下船了就是0了

check = 0  # 到9就归0
i = 1  # 控制报数
j = 0  # 控制下船了15人
while i <= 31:
    if i == 31:  # 当报数到了31，重置i为1
        i = 1
    elif j == 15:  # 当下船人数到了15，退出循环
        break
    else:
        if people[i] == 0:  # 如果这个人已经下船了
            i += 1  # 继续报数
            continue
        else:
            check += 1
            if check == 9:  # 报数到9的时候，就让人下船:
                people[i] = 0  # 下船的这个人是第几号船员，让他=0
                check = 0  # 重置check
                print("{}号下船了".format(i))
                j += 1  # 有人下船，则下船人数+1
            else:
                i += 1  # 无人下船继续报数
                continue
