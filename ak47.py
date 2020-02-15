import random
import time
i = 0
print("J=骑士，Q=皇后，K=国王，A=Ace（1）")
p1_life = 20
p2_life = 20
shelf = []
poker = ["黑桃A", "黑桃2", "黑桃3", "黑桃4", "黑桃5", "黑桃6", "黑桃7", "黑桃8", "黑桃9", "黑桃10", "黑桃J", "黑桃Q", "黑桃K",
         "红桃A", "红桃2", "红桃3", "红桃4", "红桃5", "红桃6", "红桃7", "红桃8", "红桃9", "红桃10", "红桃J", "红桃Q", "红桃K",
         "梅花A", "梅花2", "梅花3", "梅花4", "梅花5", "梅花6", "梅花7", "梅花8", "梅花9", "梅花10", "梅花J", "梅花Q", "梅花K",
         "方块A", "方块2", "方块3", "方块4", "方块5", "方块6", "方块7", "方块8", "方块9", "方块10", "方块J", "方块Q", "方块K"]


def player1():
    global p2_life
    print("p1到你了！")
    if "A" in "".join(p1) and "K" in "".join(p1) and "4" in "".join(p1) and "7" in "".join(p1):
        printerr("p1:Kalashnikov cyka!")
        dice = random.randint(1, 6)
        p2_life = p2_life - dice
        print("p2受到"+str(dice)+"伤害")
        if p2_life <= 0:
            printgreen("玩家1胜利！")
            exit()
        else:
            pass
        time.sleep(4)
    else:
        print(p1)
        remove_p1 = input("你要移除哪张牌？")
        if remove_p1 == "":
            pass
        else:
            p1_to_shelf = input("是否要放在储物架上？（y/n，默认选项为n）")
            p1.remove(remove_p1)
            if p1_to_shelf == "Y" or p1_to_shelf == "y":
                shelf.append(remove_p1)
            else:
                pass
            poker.append(remove_p1)
            take_p1 = input("是否从货架上获取？（y/n，默认选项为n）")
            if take_p1 == "Y" or take_p1 == "y":
                try:
                    if len(p1) == 4:
                        print("你的背包满了！")
                        pass
                    else:
                        while True:
                            p1_take = random.choice(shelf)
                            if p1_take in p1:
                                pass
                            else:
                                shelf.remove(p1_take)
                                p1.append(p1_take)
                                break
                except IndexError:
                    print("货架为空")
                    if len(p1) == 4:
                        pass
                    else:
                        while True:
                            p1_take = random.choice(poker)
                            if p1_take in p1:
                                pass
                            else:
                                poker.remove(p1_take)
                                p1.append(p1_take)
                                break
            else:
                if len(p1) == 4:
                    pass
                else:
                    while True:
                        p1_take = random.choice(poker)
                        if p1_take in p1:
                            pass
                        else:
                            poker.remove(p1_take)
                            p1.append(p1_take)
                            break


def player2():
    global p1_life
    print("p2到你了！")
    if "A" in "".join(p2) and "K" in "".join(p2) and "4" in "".join(p2) and "7" in "".join(p2):
        printerr("p2:Kalashnikov cyka!")
        dice = random.randint(1, 6)
        p1_life = p1_life - dice
        print("p1受到" + str(dice) + "伤害")
        if p1_life <= 0:
            printgreen("玩家2胜利！")
            exit()
        else:
            pass
        time.sleep(4)
    else:
        print(p2)
        remove_p2 = input("你要移除哪张牌？")
        if remove_p2 == "":
            pass
        else:
            p2_to_shelf = input("是否要放在储物架上？（y/n，默认选项为n）")
            p2.remove(remove_p2)
            if p2_to_shelf == "Y" or p2_to_shelf == "y":
                shelf.append(remove_p2)
            else:
                pass
            poker.append(remove_p2)
            take_p2 = input("是否从货架上获取？（y/n，默认选项为n）")
            if take_p2 == "Y" or take_p2 == "y":
                try:
                    if len(p2) == 4:
                        print("你的背包满了！")
                        pass
                    else:
                        p2_take = random.choice(shelf)
                        shelf.remove(p2_take)
                        p2.append(p2_take)
                except IndexError:
                    print("货架为空")
                    if len(p2) == 4:
                        pass
                    else:
                        while True:
                            p2_take = random.choice(poker)
                            if p2_take in p2:
                                pass
                            else:
                                poker.remove(p2_take)
                                p2.append(p2_take)
                                break
            else:
                if len(p2) == 4:
                    pass
                else:
                    while True:
                        p2_take = random.choice(poker)
                        if p2_take in p2:
                            pass
                        else:
                            poker.remove(p2_take)
                            p2.append(p2_take)
                            break


def printgreen(str):
    print("\033[32m" + str + "\033[0m")


def printerr(str):
    print("\033[31m" + str + "\033[0m")


p1 = random.sample(poker, 4)
for i in range(len(p1)):
    poker.remove(p1[i])
p2 = random.sample(poker, 4)
for i in range(len(p2)):
    poker.remove(p2[i])
while True:
    try:
        player1()
    except ValueError:
        print("无效的选项！")
        pass
    try:
        player2()
    except ValueError:
        print("无效的选项！")
        pass
