# USACO 2022 January #2: Non-Transitive Dice

k = int(input())

def win(a, b):
    score1 = 0
    score2 = 0

    for num1 in range(a):
        for num2 in range(b):
            if a[num1] > b[num2]:
                score1 += 1

            elif a[num1] < b[num2]:
                score2 += 1

for _ in k:
    dice_a, dice_b = input().split()
    a, b = win(dice_a, dice_b)
