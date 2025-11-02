# USACO 2019 January Bronze #1: Shell Game

with open("shell.in", "r+") as input_:
    in_ = input_.readlines()

for line in range(len(in_)):
    in_[line] = in_[line].strip()

print(in_)

guess_dict = {
    1: 0,
    2: 0,
    3: 0
}

location_dict = {
    # format: number: index
    1: 1,
    2: 2,
    3: 3
}

for case in range(1, int(in_[0]) + 1):
    swap1, swap2, guess_loc = [int(x) for x in in_[case].split()]    

    tmp = location_dict[swap1]
    location_dict[swap1] = location_dict[swap2]
    location_dict[swap2] = tmp

    print("location:", location_dict)
    print("guess:", guess_loc)
    guess_dict[location_dict[guess_loc]] += 1
    print("guess dict:", guess_dict)

with open("shell.out", "w+") as out:
    out.write(str(max(guess_dict.values())) + "\n")