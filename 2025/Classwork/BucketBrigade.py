# USACO 2019 US Open Contest Bronze #1: Bucket Brigade

with open("buckets.in", "r+") as input_:
    bucketsin = input_.readlines()

coords = {}

for i in range(len(bucketsin)):
    bucketsin[i] = bucketsin[i].strip()
    #print(bucketsin[i])

    for square in range(len(bucketsin)):

        if bucketsin[i][square] == 'B':
            coords['barn'] = (i, square)
        
        elif bucketsin[i][square] == 'R':
            coords['rock'] = (i, square)
        
        elif bucketsin[i][square] == 'L':
            coords['lake'] = (i, square)

sol = abs(int(coords['barn'][0]) - int(coords['lake'][0])) + abs(int(coords['barn'][1]) - int(coords['lake'][1])) - 1

if coords['rock'][0] == coords['lake'][0] and coords['barn'][0] == coords['lake'][0]:
    print('a')
    if (coords['rock'][1] < coords['barn'][1] and coords['lake'][1] < coords['rock'][1]) or (coords['rock'][1] < coords['barn'][1] and coords['lake'][1] < coords['rock'][1]):
        sol += 2

elif coords['rock'][1] == coords['lake'][1] and coords['barn'][1] == coords['lake'][1]:
    print('b')
    if (coords['rock'][0] < coords['barn'][0] and coords['lake'][0] < coords['rock'][0]) or (coords['rock'][0] > coords['barn'][0] and coords['lake'][0] > coords['rock'][0]):
        sol += 2

out = open('buckets.out', 'w+')
out.write(str(sol))