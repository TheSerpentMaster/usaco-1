# USACO February US Open Contest Bronze #3: Measuring Traffic

with open("traffic.in", 'r+') as inp:
    lines = inp.readlines()

    n = int(lines[0].strip())
    segments = []
    for line_ in lines[1:]:
        line = line_.split()

        ramp_type, min_speed, max_speed = line[0], int(line[1]), int(line[2])
        segments.append([ramp_type, min_speed, max_speed])

mins = -9999999
maxs = 9999999

for segment in range(len(segments)):# - 1, -1, -1):
    segm = segments[segment]
    
    if segm[0] == 'on':
        mins += segm[1]
        if mins < 0:
            mins = 0
        maxs += segm[2]
        if maxs < 0:
            maxs = 0
    
    elif segm[0] == 'off':
        mins -= segm[2]
        if mins < 0:
            mins = 0
        maxs -= segm[1]
        if maxs < 0:
            maxs = 0
    
    else:
        mins = max(mins, segm[1])
        if mins < 0:
            mins = 0
        maxs = min(maxs, segm[2])
        if maxs < 0:
            maxs = 0

outflow = str(mins) + ' ' + str(maxs) + '\n'

mins = -9999999
maxs = 9999999

for segment in range(len(segments) - 1, -1, -1):
    segm = segments[segment]
    
    if segm[0] == 'on':
        mins -= segm[2]
        if mins < 0:
            mins = 0
        maxs -= segm[1]
        if maxs < 0:
            maxs = 0
    
    elif segm[0] == 'off':
        mins += segm[1]
        maxs += segm[2]
    
    else:
        mins = max(mins, segm[1])
        if mins < 0:
            mins = 0
        maxs = min(maxs, segm[2])
        if maxs < 0:
            maxs = 0

inflow = str(mins) + ' ' + str(maxs) + '\n'

with open("traffic.out", 'w+') as out:
    out.write(inflow + outflow)