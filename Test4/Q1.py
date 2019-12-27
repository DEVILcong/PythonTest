#! /usr/bin/env python3

def chstr2num(chstr):
    num = {'一':1, '二':2, '三':3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9, '壹':1, '贰':2, '叁':3, '肆':4, '伍':5, '陆':6, '柒':7, '捌':8, '玖':9}
    big = {'零':0, '十':10, '百':100, '千':1000, '万':10000, '拾':10, '佰':100, '仟':1000, '萬':10000}

    trueNum = 0
    if chstr[0] in num and (chstr[1] in num or chstr[1] == '零'):
        trueNum = []
        for i in chstr:
            if i in num:
                trueNum.append(str(num[i]))
            else:
                trueNum.append(str(big[i]))
        trueNum = int(''.join(trueNum))
    else:
        i = 0
        while(i < len(chstr)):
            if chstr[i] == '点':  #五十四万点四的情况
                break
            elif (i + 1 == len(chstr) or chstr[i+1] == '点') and chstr[i] in num: #十万点四的情况
                trueNum += num[chstr[i]]
                i += 1
                break
            else:
                if chstr[i] in num:
                    if chstr[i + 1] == '万' or chstr[i + 1] == '萬':  #五十四万、十万零四等情况
                        trueNum = (trueNum + num[chstr[i]])*10000
                    else:
                        trueNum += num[chstr[i]] * big[chstr[i + 1]]
                    i += 2
                else:
                    if chstr[i] == '万' or chstr[i] == '萬':
                        trueNum = trueNum * 10000
                        i += 1
                    elif chstr[i + 1] == '万' or chstr[i + 1] == '萬':
                        trueNum += big[chstr[i]] * 10000
                        i += 2
                    else:
                        trueNum += big[chstr[i]]
                        i += 1
    if i != len(chstr):  #小数点后
        i += 1
        orii = i-1
        trueNum = float(trueNum)
        while i < len(chstr):
            if chstr[i] in num:
                trueNum += num[chstr[i]] * (10 ** -(i - orii))
            else:
                trueNum += big[chstr[i]] * (10 ** -(i - orii))
            i += i
    return trueNum
