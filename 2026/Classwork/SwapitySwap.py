# USACO 2020 February Contest Bronze #3: Swapity Swap

with open('swap.in', 'r') as inp:
    a = inp.read().split('\n')[:-1]

def reverse(arr, start, end):
    start -= 1
    end -= 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr

N, K = a[0].split()
N = int(N)
K = int(K)
one, two = a[1].split()
one = int(one)
two = int(two)
three, four = a[2].split()
three = int(three)
four = int(four)

starter = [i for i in range(1, N + 1)]

for i in range(K):
    starter = reverse(starter, one, two)
    starter = reverse(starter, three, four)

for i in range(len(starter)):
    starter[i] = str(starter[i])

with open("swap.out", 'w') as out:
    out.write('\n'.join(starter) + '\n')