#! /usr/bin/env python3
# coding:utf8

def handleList(L):
    add = 0
    for i in range(len(L)):
        add += L[i]
    avg = add / len(L)

    midList = sorted(L)
    midNum = 0
    if len(L) % 2 == 0:
        midNum = (midList[int(len(L)/2)] + midList[int(len(L)/2-1)]) / 2
    else:
        midNum = midList[int(len(L)/2)]

    add = add - midList.pop(0)
    add = add - midList.pop(-1)
    add = add / len(midList)

    print('传入列表为：', L)
    print('平均值：%f, 中位数：%f，去掉最大最小值后的平均值：%f'%(avg, midNum, add))


a = [1, 2, 10, 3, 5, 0]
handleList(a)
