import math

N = int(input())
output = []

def sleepconstant(input_: list, number: int):
    steps = 0
    a = 0

    for num in input_:
        a += num

        if a == number:
            a = 0
            steps -= 1
 
        elif a > number:
            return False
        
        steps += 1
    
    return steps

def factorize(num: int):
    i = 1
    number = num
    factors = []

    while i <= math.sqrt(num):
        if number % i == 0:
            factors.append(i)
            factors.append(int(num / i))
        i += 1
    
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
    factors.sort()
    #print(factors)

    for factor in factors:
        sleep = sleepconstant(classes, factor)
        #print("sleep", sleep)
        
        if sleep:
            output.append(sleep)
            break

    if len(output) == case:
        output.append(len(classes) - 1)

#print(output)

for case in output:
    print(case)