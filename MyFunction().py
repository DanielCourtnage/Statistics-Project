def myfunction():
    dice = 6
    for i in range(0, dice):
        while dice > 0:
            for i in range(0, dice):
                roll = (random.randint(1, 6))
                list.append(roll)
            count_x = list.count(x)
            count_y = list.count(y)
            for i in range(count_x):
                list.remove(x)
            for i in range(count_y):
                list.remove(y)
            dice = dice - count_x - count_y
        if dice <= 0:
            break
