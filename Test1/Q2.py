#! /usr/bin/env python3
#coding:utf8

import math
import random

def isInCircle(x, y):
    if math.sqrt(x**2 + y**2) < 1:
        return True
    else:
        return False

def getPi(num):
    times = 0
    for i in range(num):
        if isInCircle(random.uniform(-1, 1), random.uniform(-1, 1)):
            times+=1
    
    return (times/num)*4

print(getPi(1000000))
