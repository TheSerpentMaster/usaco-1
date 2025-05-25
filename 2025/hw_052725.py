import math

N = int(input())
output = []

def isprime(num: int):
    i = 2
    number = num
    factors = {}

    while i < math.sqrt(num):
        if number % i == 0:
            if i in factors.keys():
                factors[i] += 1
                number /= i
                
                if (number / i) in factors.keys():
                    factors[number / i] += 1
                    number /= (number / i)
                
                else:
                    factors[number / i] = 1
                    number /= (number / i)
            
            else:
                factors[i] = 1
                number /= i

                if (number / i) in factors.keys():
                    factors[number / i] += 1
                    number /= (number / i)
                
                else:
                    factors[number / i] = 1
                    number /= (number / i)
        
        else:
            i += 1
    
    return factors



for case in output:
    print(case)