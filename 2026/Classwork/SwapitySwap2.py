# USACO 2020 February Contest Bronze #3: Swapity Swap

with open('swap.in', 'r') as inp:
    a = inp.read().split('\n')[:-1]

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr

def swap(arr, one, two):
    arr[one], arr[two] = arr[two], arr[one]
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

starter = [i for i in range(0, N + 1)]

starter = reverse(starter, one, two)
starter = reverse(starter, three, four)
print(starter)

previous = starter.copy()
previous2 = previous.copy()

j = 0

while previous2 != [i for i in range(0, N + 1)]:
    j += 1
    previous2 = reverse(previous2, one, two)
    previous2 = reverse(previous2, three, four)
    print(previous2)

for i in range((K-1) % (j + 1)):
    starter = reverse(starter, one, two)
    starter = reverse(starter, three, four)

print(j)
#print(starter)

with open("swap.out", 'w') as out:
    out.write('\n'.join([str(i) for i in starter[1:]]) + '\n')