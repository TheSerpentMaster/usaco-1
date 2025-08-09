# USACO 2022 February US Open Bronze #1: Photoshoot

N = int(input())

input_list = input()
output_list = ['A']

for i in range(0, len(input_list), 2):
    combo = input_list[i:i+2]

    if combo == 'HG':
        if output_list[-1] != 'C':
            output_list.append('C')

    elif combo == 'GH':
        if output_list[-1] != 'B':
            output_list.append('B')

output_list.pop(0)

if output_list[-1] == 'C':
    print(len(output_list) - 1)

else:
    print(len(output_list))