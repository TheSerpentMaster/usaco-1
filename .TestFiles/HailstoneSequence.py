num = 5

def Hailstone1(number):
    if number == 1:
        num += 1
        return Hailstone2(num)

    elif number % 2 == 0:
        return Hailstone2(number // 2)

    else:
        return Hailstone2(3 * number + 1)

def Hailstone2(number):
    if number == 1:
        num += 1
        return Hailstone1(num)

    elif number % 2 == 0:
        return 1 + Hailstone2(number // 2)

    else:
        return 1 + Hailstone2(3 * number + 1)

def Hailstone2(number):
    if number == 1:
        num += 1
        return Hailstone1(num)
    
    elif number % 2 == 0:
        return 1 + Hailstone2(number // 2)
    
    else:
        return 1 + Hailstone2(3 * number + 1)

print(Hailstone1(num))