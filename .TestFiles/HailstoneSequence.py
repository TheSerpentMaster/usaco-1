def Hailstone1(number):
    if number % 2 == 0:
        print(number // 2)
        if number // 2 == 1:
            number += 1
    
        return Hailstone2(number // 2)

def Hailstone2(number):
    pass

Hailstone1(5)