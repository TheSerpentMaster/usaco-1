# Test dummy file

import math

def update_need(need: dict, recipes: dict, missing):
    if missing != {}:
        for metal in list(missing.keys()):
            print(recipes)
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

print(update_need({3: 1, 4: 1}, {2: [1], 3: [2], 4: [3]}, {3: 1, 4: 1}))  # prints {1: 1, 2: 2}