#! /usr/bin/env python3
# coding:utf8

top = 1
bottem = 1

x = input('please input a num:')
x = float(x)
powX = x
result = 0
flag = -1

for i in range(2):
    flag = flag * -1

    if i == 0:
        result += flag * (powX / (2*i+1))
    else:
        top = top * (2*i-1)
        bottem = bottem * 2 * i
        result += flag * (top / bottem) * (powX / (2*i+1))

    powX = powX * x**2

print(result)


