# USACO February US Open Contest Bronze #3: Alchemy

N = int(input())
metals = input().split()
K = int(input())

total_n_metals = 0

recipes = {}
inventory = {}
need = {N: 1}

def missing(need: dict, inventory: dict):
    missing = {}

    for metal in need.keys():
        if metal not in inventory.keys():
            missing[metal] = need[metal]
        
        elif inventory[metal] < need[metal]:
            missing[metal] = need[metal] - inventory[metal]
        
    return missing

def update_need(need: dict, recipes: dict, missing):
    if missing != {}:
        for metal in list(missing.keys()):
            if metal in recipes.keys():
                for element in recipes[metal]:
                    if element in need.keys():
                        need[element] += missing[metal]
                    
                    else:
                        need[element] = missing[metal]

            else:
                return False

            need[metal] -= missing[metal]

            if need[metal] == 0:
                del need[metal]

        return need
    
    return need

def inventory_update(current_need: dict, inventory: dict):
    for metal in current_need.keys():
        if metal in inventory.keys():
            if inventory[metal] < current_need[metal]:
                del inventory[metal]
                
            else:
                inventory[metal] -= current_need[metal]
    
    return inventory

for element in range(0, len(metals) + 1):
    inventory[element] = int(metals[element - 1])

for i in range(N):
    for element in range(len(metals)):
        if metals[element] == i:
            if i not in inventory.keys():
                inventory[i] = 1
            
            else:
                inventory[i] += 1

for _ in range(K):
    recipe = input().split()

    for element in range(len(recipe)):
        recipe[element] = int(recipe[element])
    
    recipes[recipe[0]] = recipe[2:]

current_need = need.copy()

while current_need:
    inventory_copy = inventory.copy()
    missing_metals = missing(current_need, inventory_copy)
    #print(missing_metals)

    if missing_metals != {}:
        current_need = update_need(current_need, recipes, missing_metals)
        #print(current_need)

    else:
        inventory = inventory_update(current_need, inventory_copy)
        total_n_metals += 1

print(total_n_metals)