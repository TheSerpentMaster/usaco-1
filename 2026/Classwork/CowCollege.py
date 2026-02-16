# USACO 2022 December Bronze #1: Cow College

n = int(input())
cows = input().split()

for cow in range(len(cows)):
    cows[cow] = int(cows[cow])

cows.sort(reverse = True)
setcows = list(set(cows.copy()))

cows_dict = {}

for cow in cows:
    if cow in (cows_dict.keys()):
        cows_dict[cow] += 1
    
    else:
        cows_dict[cow] = 1

tuition = 0
cow_amount = 0

for cow in range(len(list(cows_dict.keys()))):
    new_tuition = cows_dict[cows[cow]] * cows[cow]
    
    if new_tuition > tuition:# and cow_amount < cows_dict[cows[cow]]:
        tuition = new_tuition
        
        cow_amount = cows_dict[cows[cow]]
        
print(tuition, cow_amount)