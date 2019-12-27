#! /usr/bin/env python3
#coding:utf8

'''
设计思路：规定四个元组，分别存储小写、大写、数字、特殊符号；通过从这四个元组中随机选取元素形成密码。随机选取阶段，for循环循环密码长度次，每次生成一个0到1之间的随机数，如果该数0-0.25，从小写中取，并将tag中小写对应的标记置1,表示已经取过小写，余下的类似。for循环结束后，判断tag中是否有三位以上为1，若是则返回密码，若不是则从每取到过的元组取一个元素，替换到密码的随机位置
'''

import string
import random

def mkPasswd(length):
    lowCase = tuple(string.ascii_lowercase)
    upCase = tuple(string.ascii_uppercase)
    digits = tuple(string.digits)
    punc = tuple(string.punctuation)
    store = (lowCase, upCase, digits, punc)
    tag = [0, 0, 0, 0]
    passwd = []

    for i in range(length):
        rand = random.uniform(0, 1)

        if rand < 0.25:
            passwd.append(random.choices(store[0])[0])
            tag[0] = 1
        elif rand > 0.25 and rand < 0.5:
            passwd.append(random.choices(store[1])[0])
            tag[1] = 1
        elif rand > 0.5 and rand < 0.75:
            passwd.append(random.choices(store[2])[0])
            tag[2] = 1
        else:
            passwd.append(random.choices(store[3])[0])
            tag[3] = 1

    plus = tag[0] + tag[1] + tag[2] + tag[3]
#print(passwd)

    if plus >= 3:
        return ''.join(passwd)
    else:
        for i in range(4):
            if tag[i] == 0:
                passwd[random.randint(0, len(passwd))] = random.choices(store[i])[0]
        return ''.join(passwd)


a = mkPasswd(20)
print(a)



 
