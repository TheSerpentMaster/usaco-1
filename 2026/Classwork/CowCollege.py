# USACO 2022 December Bronze #1: Cow College

n = int(input())
cows = input().split()

for cow in range(len(cows)):
    cows[cow] = int(cows[cow])

cows.sort()
#print(cows)

setcows = list(set(cows))
setcows.sort()

cows_dict = {}

for cow in cows:
    if cow in (cows_dict.keys()):
        cows_dict[cow] += 1

    else:
        cows_dict[cow] = 1

#print(cows_dict)

tuition = 0
cow_amount = 0
temp_cow = 0

for cow in range(len(setcows) - 1, -1, -1):
    temp_cow += cows_dict[setcows[cow]]
    new_tuition = temp_cow * setcows[cow]
    
    if new_tuition >= tuition:
        tuition = new_tuition
        cow_amount = temp_cow
    #print(new_tuition)

cow_tui = int(tuition // cow_amount)

print(tuition, cow_tui)
