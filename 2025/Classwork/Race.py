# USACO 2020 January Bronze #3: Race

K, N = input().split()

K = int(K)
N = int(N)

for i in range(N):
    X = int(input())

    length_left = K
    length_left -= X

    time = 0

    speed = 1

    while length_left > 0:
        if time == 0:
            length_left -= speed
            time += 1
            continue

        pass