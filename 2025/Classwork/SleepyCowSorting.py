# USACO 2019 January Bronze #2: Sleepy Cow Sorting

count = 0
with open("sleepy.in", 'r') as read:
    input_ = read.read().strip().split()

N = input_[0]
#print(input_)

cows = input_[1:]
#print(cows)

for cow in range(len(cows)):
    cows[cow] = int(cows[cow])

front = cows[0]
cows.remove(front)
#print(front, cows)

while True:
    break_ = False

    for cow in range(len(cows) - 1, -2, -1):
        if cow == -1:
            break_ = True

        if cow == len(cows) - 1:
            if front > cows[cow]:
                cows.append(front)
                front = cows[0]
                cows.remove(cows[0])
                break

            else:
                continue
        
        if cows[cow] > front and cows[cow + 1] < cows[cow]:
            cows.insert(cow + 1, front)
            front = cows[0]
            cows.remove(cows[0])
            break

        elif cows[cow] > front and cows[cow + 1] > cows[cow]:
            continue

        else:
            cowstorage = cows[0]
            cows.insert(cow + 1, front)
            cows.remove(cows[0])
            front = cowstorage
            break

    print([front] + cows)
    
    if break_:
        break
    
    count += 1
with open("sleepy.out", 'a+') as out:
    out.write(str(count) + '\n')