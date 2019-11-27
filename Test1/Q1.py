#! /usr/bin/env python3
#coding:utf8

seq = [1, 1]
ratio = [1]

for i in range(38):
    seq.append(seq[-1] + seq[-2])
    ratio.append(seq[-1]/seq[-2])

print(seq)
print(ratio)
