# USACO February US Open Contest Bronze #3: Measuring Traffic

with open("traffic.in", 'r+') as inp:
    lines = inp.readlines()

    n = int(lines[0].strip())
    segments = []
    for line_ in lines[1:]:
        line = line_.split()

        ramp_type, min_speed, max_speed = line[0], int(line[1]), int(line[2])
        segments.append([ramp_type, min_speed, max_speed])

mins = 0
maxs = 1001
entrance = [0, 0]
exit_ = [0, 0]

for seg in range(len(segments)):
    segm = segments[seg]
    
    if segm[0] == 'on':
        entrance[0] += segm[1]
        entrance[0] += segm[2]
        
    elif segm[0] == 'off':
        exit_[0] += segm[1]
        exit_[0] += segm[2]
    
    elif segm[0] == 'none':
        if entrance != [0, 0]:
            segm[1] -= entrance[1]
            segm[2] -= entrance[0]
        
        if exit_ != [0, 0]:
            segm[1] += exit_[1]
            segm[2] += exit_[0]
        
        mins, maxs = max(mins, segm[1]), min(maxs, segm[2])

print(mins, maxs, "a")

with open("traffic.out", "w+") as w:
    w.write(str(mins) + " " + str(maxs) + "\n" + str(mins + entrance[1] - exit_[0]) + " " + str(maxs + entrance[0] - exit_[0]) + '\n')
