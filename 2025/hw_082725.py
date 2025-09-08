#USACO 2024 February Bronze #1: Palindrome Game

N = int(input())
output = []

for i in range(N):
    in_ = int(input())

    if in_ < 10:
        output.append('B')
    
    elif in_ % 10 == 0:
        output.append('E')

    else:
        output.append('B')

for i in output:
    print(i)