# USACO 2020 January Bronze #3: Race

import math

with open('race.in', 'r+') as race:
    race_input = race.read().split('\n')

K, N = race_input[0].split()

output = []
K = int(K)
N = int(N)

for i in range(1, N + 1):
    end = race_input[i]
    end = int(end)

    distance_sum = end * (end + 1) / 2
    time = end

    if end == 1 and K <= 4:
        if K == 1:
            output.append('1')
            continue
        
        elif K == 2:
            output.append('2')
            continue

        elif K == 3 or K == 4:
            output.append('3')
            continue

    max_terms = end

    sumtest = 0
    sumtest_idx = 0

    if distance_sum > K:
        for term in range(1, end + 1):
            sumtest += term
            sumtest_idx += 1
            if sumtest >= K:
                output.append(str(sumtest_idx))
                break

        continue

    elif distance_sum == K:
        output.append(str(time))
        continue

    if K > 4 and end == 1:
        distance_sum = 4
        max_terms = 2
        time = 3

    max_terms = math.floor(math.sqrt(K + (end * (end - 1)) / 2))
    time = 2 * max_terms - end
    distance_sum = max_terms ** 2 - ((end * (end - 1)) / 2)

    while distance_sum < K:
        if K - distance_sum == (2 * max_terms) + 1:
            time += 2
            break

        elif K - distance_sum > (2 * max_terms) + 1:
            time += 2
            max_terms += 1
            distance_sum += (2 * max_terms) - 1

        elif K - distance_sum > max_terms:
            time += 1
            distance_sum += max_terms
        
        elif K - distance_sum == max_terms:
            time += 1
            break

        else:
            time += 1
            break

    output.append(str(time))

with open('race.out', 'a+') as out:
    out.write('\n'.join(output) + '\n')
