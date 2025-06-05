import math

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

print(factorize(91))