# USACO 2022 January #2: Non-Transitive Dice

k = int(input())
results = []

def win(a, b):
    score1 = 0
    score2 = 0
    
    for num1 in range(len(a)):
        for num2 in range(len(b)):
            if a[num1] > b[num2]:
                score1 += 1
            
            elif a[num1] < b[num2]:
                score2 += 1

    if score1 > score2:
        return a, b
    
    elif score2 > score1:
        return b, a
    
    else:
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

    if winning:
        a, b = winning

        done = False

        for num1 in range(10):
            for num2 in range(10):
                for num3 in range(10):
                    for num4 in range(10):
                        dice = [num1, num2, num3, num4]

                        if (win(a, dice)) == (dice, a):
                            if win(b, dice) == (b, dice):
                                #print(a, b, dice)
                                results.append('yes')
                                done = True
                                break

                    if done:
                        break
                if done:
                    break
            if done:
                break
        #print(len(results), k)
        if len(results) < k:
            results.append('no')           
                        
    else:
        results.append('no')

for i in results:
    print(i)