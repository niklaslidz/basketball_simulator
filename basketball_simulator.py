import random


class Player:
    def __init__(self,name,choose,three_rate,two_rate):
        self.name = name
        self.choose = choose
        self.three_rate = three_rate
        self.two_rate = two_rate

    def shoot(self):
        a = random.randint(1,100)
        b = random.randint(1,100)
        if 1 <= a <= int(self.choose):
            print("%s三分出手"% self.name)
            if 1 <= b <= int(self.three_rate):
                print("%s三分命中" % self.name)
            else:
                print("三分不中")
        else:
            print("%s中距离出手" % self.name)
            if 1 <= b <= int(self.two_rate):
                print("%s两分命中" % self.name)
            else:
                print("两分不中")

    def dunk(self):
        b = random.randint(1,100)
        if 1 <= b <= int(self.two_rate):
            print("%s一记爆扣,两分入账"% self.name)
        else:
            print("%s惨遭血帽" % self.name)


def main():
    James = Player("詹姆斯","19","35","51")
    Love = Player("勒夫","38","33","33")
    TT = Player("TT","0","0","54")
    Irving = Player("欧文","22","41","51")
    Smith = Player("JR","65","38","39")
    Curry = Player("库里","51","40","47")
    Thompson = Player("汤普森","49","37","46")
    Durant = Player("杜兰特","24","45","52")
    Green = Player("格林","35","31","47")
    Looney = Player("鲁尼","0","0","59")
    print("比赛开始")
    sum_time = 2880

    while sum_time > 0:
        x = random.randint(1,100)
        if 1 <= x <= 29:
            Curry.shoot()
        elif 29 <= x <=59:
            Durant.shoot()
        elif 59 <= x <=80:
            Thompson.shoot()
        elif 80 <= x <= 85:
            Looney.dunk()
        else:
            Green.dunk()

        y = random.randint(1,100)
        if 1 <= y <= 34:
            James.shoot()
        elif 34 <= y <= 65:
            Irving.shoot()
        elif 65 <= y <= 77:
            Smith.shoot()
        elif 77 <= y <= 91:
            Love.shoot()
        else:
            TT.dunk()
        print()
        sum_time -= 24
    print("比赛结束")


main()


