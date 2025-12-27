# USACO 2022 January #2: Non-Transitive Dice

k = int(input())
results = []

def win(a, b):
    score1 = 0
    score2 = 0

    for num1 in a:
        for num2 in b:
            if num1 > num2:
                score1 += 1
            elif num1 < num2:
                score2 += 1

    if score1 > score2:
        return 1
    if score1 < score2:
        return -1
    return 0

def find(a, b):
    for x in range(1, 11):
        for y in range(1, 11):
            for z in range(1, 11):
                for k in range(1, 11):
                    dice = (x, y, z, k)
                    if win(dice, a) == 1 and win(b, dice) == 1:
                        return True
    return False

for _ in range(k):
    dice = input().split()

    dice_a = dice[:4]
    dice_b = dice[4:]

    for i in range(len(dice_a)):
        dice_a[i] = int(dice_a[i])
    for i in range(len(dice_b)):
        dice_b[i] = int(dice_b[i])

    winning = win(dice_a, dice_b)

    if winning == 0:
        results.append("no")
    elif winning == 1 and find(dice_a, dice_b):
        results.append("yes")
    elif winning == -1 and find(dice_b, dice_a):
        results.append("yes")
    else:
        results.append("no")

for i in results:
    print(i)