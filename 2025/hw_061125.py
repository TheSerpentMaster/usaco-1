# USACO February US Open Contest Bronze #3: Alchemy

N = int(input())
metals = input().split()
K = int(input())

recipes = {}

for metal in range(len(metals)):
    metals[metal] = int(metals[metal])

for _ in range(K):
    recipe = input().split()

    for element in range(len(recipe)):
        recipe[element] = int(recipe[element])
    
    recipes[recipe[0]] = recipe[2:]

