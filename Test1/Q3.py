#! /usr/bin/env python3
#coding:utf8

def shopping(itemList):

    item = 0
    num = 0
    check = 0
    print('请输入商品名及购买数量，以逗号分开，输入为空结束')

    while True:
        middle = input()
        if middle == '':
            break
        item,num = middle.split(',')
        num = int(num)
	    
        if not item in itemList:
            continue

        check += itemList[item] * num
    return check


itemList = {'a':3, 'b':4, 'c':5}
print(shopping(itemList))
