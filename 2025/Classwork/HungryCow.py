# USACO 2023 February Bronze #1: Hungry Cow

N, T = input().split()

food_days = 0
runs_out = -1

for i in range(int(N)):
    day, food = input().split()

    day = int(day)
    food = int(food)
    
    if day + food > int(T):
        #print('e')
        #print(food)
        food = int(T) - day + 1

    if runs_out >= day:
        food_days -= 1

    if food_days > day:
        food_days += food - food_days
        runs_out = day + food - food_days
    
    elif food_days == day:
        food_days += food - 1
        runs_out = day + food - 1
    
    else:
        food_days += food
        runs_out = day + food

if food_days > int(T):
    food_days = int(T)

print(food_days)