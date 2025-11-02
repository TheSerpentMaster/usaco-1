#USACO 2019 February Contest #1: Sleepy Cow Herding

res = 0

with open("herding.in", "r") as inp:
    cows = inp.read().split()

for i in range(len(cows)):
    cows[i] = int(cows[i])

cows.sort()

if cows[2] - cows[0] == 2:
    res = 0

elif (abs(cows[0] - cows[1]) == 2) or (abs(cows[1] - cows[2]) == 2):
    res = 1

else:
    res = 2


if (cows[2] - cows[1]) >= 2 and (cows[1] - cows[0]) <= (cows[2] - cows[1]):
    maxi = cows[2] - cows[1] - 1
else:
    maxi = cows[1] - cows[0] - 1

with open('herding.out', 'w+') as out:
    out.write(str(res) + f'\n{str(maxi)}\n')