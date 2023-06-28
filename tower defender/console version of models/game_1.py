import random
balance = 1000
def game(x):
    global balance
    chance = random.random() * 100
    if chance <= 3:
        x = x * 36
        print("вы выиграли, и заработали "+ str(x) + " монет!")
        balance += x
    else:
        print("вы проиграли " + str(x) + " монет!")
        balance -= x
while True:
    print("ваш баланс:" + str(balance))
    try:
        bet = input("ваша ставка:")
        bet = int(bet)
        if bet > balance:
            print("вы не можете поставить игровые монеты больше игрового баланса.\n вы можете поставить весь ваш баланс. введите 0 чтобы ввести заново,\nи 1 чтобы поставить весь баланс")
            answer = input("введите ответ:")
            answer = int(answer)
            if answer == 0:
                bet = input("ваша ставка:")
                bet = int(bet)
                game(bet)
            else:
                game(balance)
        game(bet)
    except ValueError:
        print("то, что вы ввели -- не число")
