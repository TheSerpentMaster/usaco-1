## USACO 2021 January Contest Bronze #3: Measuring Traffic

n = int(input())
count = 1
countlist = []

for i in range(n):
    countlist.append(0)

cows = input().split()
stalls = input().split()

stalls.sort()

for cow in range(n):
    cows[cow] = int(cows[cow])

for stall in range(n):
    stalls[stall] = int(stalls[stall])

for cow in range(len(cows)):
    for stall in range(len(stalls)):
        if cows[cow] <= stalls[stall]:
            countlist[stall] += 1


for i in range(len(cows)):
    count = count*(countlist[i]-i)

print(count)