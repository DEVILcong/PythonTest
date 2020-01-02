#coding:utf8
import random

class stupidRobot:
    def __init__(self):
        self._name = input('请输入你的名字:')
        print('欢迎你', self._name)

    def joke(self):
        print(random.choice(self._joke))

    def calculator(self):
        process = input('请输入算式，例如3*4:')

        pro = ['+', '-', '*', '/']
        a = 0
        for i in pro:
            if(len(process.split(i)) == 2):
                process = process.split(i)
                break
            else:
                a+=1
        if a == 4:
            print('对不起，不知道你在说什么')
            return

        num1 = int(process[0])
        num2 = int(process[1])
        if a == 0:
            num1 = num1 + num2
        elif a == 1:
            num1 = num1 - num2
        elif a == 2:
            num1 = num1 * num2
        else:
            num1 = num1 / num2
        print('运算结果为：', num1)

    def game(self):
        print('猜数字游戏，1-50之间，输入50以上结束游戏')
        num = random.randint(1, 50)
        times = 0
        numIn = -1
        while num != numIn and numIn < 51:
            numIn = input('猜一个数吧:')
            numIn = int(numIn)
            if numIn > num:
                print('太大了')
            elif numIn < num:
                print('太小了')
            else:
                print('恭喜你，猜对了')
                break

            if times > 10:
                print('你好笨，现在还没猜出来')

            times += 1

    def run(self):
        func = ''
        while func != '退出':
            func = input('选择一个功能吧（讲笑话，计算器，玩游戏，退出）:')
            
            if func == '讲笑话':
                self.joke()
            elif func == '玩游戏':
                self.game()
            elif func == '计算器':
                self.calculator()
            elif func == '退出':
                break
            else:
                print('我不知道你在说什么')

        print('再见了', self._name)

    _name = ''
    _joke = ['一只癞蛤蟆最新茶不思饭不想，连蚊子都不抓着吃了，其他的癞蛤蟆都很想知道它到底怎么了。年最长癞蛤蟆说了：“抓只天鹅来，保管好。因为癞蛤蟆想吃天鹅肉呀', '一次五岁的儿子问我，我手上拿着的东西是什么，我说是手机，他说为什么叫手机那，我那时正忙就随口唱到“左手一只鸡，右手一只鸭。”儿子露出更加疑惑的表情：“那为什么不叫手鸭那？', '我和朋友走到分岔路口，我们以歌作别：“我送你离开，千里之外。”于是，“千里之外”就走了', '一MM失恋了，几次欲寻短见都被亲友及时发现未能实现。一日趁亲友不备离家出走，急的亲友到处寻找，就在决定报警时，收到她发来的短信：你们不必找我了，我在去往死海的路上，我喜欢大海，我决定在那儿结束我的人生', '阿钜要考试，妈妈问阿钜书看完了吗？阿钜说：“我看完了。”第二天妈妈看到阿钜不及格的卷子大发雷霆，“你书都看了为什么考这么差！”阿钜：“妈妈，我那天说的是。。。我看，完了', '人家不想讲']
