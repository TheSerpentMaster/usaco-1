import math

def sleepconstant(input_: list, number: int):
    a = 0
    count = 0

    for num in input_:
        a += num
        count += 1

        if a == number:
            count -= 1
            a = 0

        elif a > number:
            return False
    
    if a != 0:
        return False

    return count

print(sleepconstant([2, 2, 3], 3))