# USACO 2022 January Bronze #2: Cannonball

N, S = input().split()

N = int(N)
S = int(S)

line = {}
broken = {}
travelbook = {}
count = 0

for num in range(N):
    q, v = input().split()
    
    q = int(q)
    v = int(v)
    
    line[num] = [q, v]

speed = 1
location = S - 1
direction = 1

#print(line[location])

if line[location][0] == 0:
    speed += line[location][1]
    direction *= -1

else:
    if line[location][1] <= speed:
        broken[location] = 1

location += speed * direction
travelbook[(location, speed, direction)] = 1

#print("speed, location:", speed, location)

while location >= 0 and location <= N - 1:
    #print("type:", line[location][0], "v:", line[location][1])
    if line[location][0] == 0:
        # Jump pad
        speed += line[location][1]
        direction *= -1
    
    else:
        # Target
        if speed >= line[location][1] and location not in broken:
            broken[location] = 1
            #print(broken)

    location += speed * direction

    if (location, speed, direction) not in travelbook:
        travelbook[(location, speed, direction)] = 1
    
    else:
        break
    #print("speed, location:", speed, location)

print(len(broken))