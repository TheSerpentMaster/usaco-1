# USACO 2023 February Bronze #1: Hungry Cow

N, T = input().split()
N, T = int(N), int(T)

temp = 0
no_food = 1
count = 0

for i in range(N):
    day, food = input().split()

    day = int(day)
    food = int(food)
    
    if day > no_food:
        no_food = day

    temp = no_food + food - 1
    new_food = temp + 1

    if new_food > T:
        count += T - no_food + 1
        break

    count += food
    no_food = new_food

print(count)