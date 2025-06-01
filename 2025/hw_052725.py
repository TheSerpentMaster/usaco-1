import math

N = int(input())
output = []

def calc_exp(factors: dict):
    count = 0
    count = str(count)

    while True:
        for digit in range(len(count)):
            if int(count[digit]) + 1 == factors.keys()[digit]:
                if digit == len(count) - 1:
                    break
                
            count[digit] = str(int(digit + 1))

def sleepconstant(input_: list, number: int):
    a = 0

    for num in input_:
        a += num

        if a == number:
            a = 0

        elif a > number:
            return False
    
    return True

def factorize(num: int):
    i = 2
    number = num
    factors = {}

    while i <= math.sqrt(num):
        if number % i == 0:
            if i in factors.keys():
                factors[i] += 1
                number /= i
            
            else:
                factors[i] = 1
                number /= i

        else:
            i += 1
        
    if number > 1:
        factors[int(number)] = 1
    
    return factors

for case in range(N):
    lencase = int(input())
    classes = input().split()

    if set(classes) == set(classes[0]):
        output.append(0)

        continue

    for num in range(len(classes)):
        classes[num] = int(classes[num])

    factors = factorize(sum(classes))

    num = 1
    for factor in list(factors.keys()):
        for _ in range(1, factors[factor] + 1):
            num *= factor
            sleep = sleepconstant(classes, num)

            if sleep:
                output.append(sleep)
                break
            
    output.append(len(classes))

for case in output:
    print(case)