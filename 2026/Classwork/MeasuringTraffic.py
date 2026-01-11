# USACO February US Open Contest Bronze #3: Measuring Traffic

with open("traffic.in", 'r') as inp:
    n = int(inp.readlines()[0].strip())
    print(n)
    segments = []
    print(inp.readlines())
    
    lines = inp.readlines()[1:]
    print(lines)
    for line_ in lines:
        line = line_.split()
        print(line)

        ramp_type, min_speed, max_speed = line[0], int(line[1]), int(line[2])
        segments.append((ramp_type, min_speed, max_speed))

low = [0] * n
current_low = 0

for i in range(n):
    ramp_type, min_speed, max_speed = segments[i]

    if ramp_type == 'on':
        current_low = max(current_low, min_speed)

    elif ramp_type == 'off':
        current_low = max(current_low, min_speed)

    elif ramp_type == 'none':
        current_low = max(current_low, min_speed)

    low[i] = current_low

high = [10 ** 9 + 1] * n
current_high = 10 ** 9 + 1

for i in range(n - 1, -1, -1):
    ramp_type, min_speed, max_speed = segments[i]

    if ramp_type == 'on':
        current_high = min(current_high, max_speed)
    
    elif ramp_type == 'off':
        current_high = min(current_high, max_speed)
    
    elif ramp_type == 'none':
        current_high = min(current_high, max_speed)
    
    high[i] = current_high

output = "\n".join(f"{low[i]} {high[i]}" for i in range(n))

with open("traffic.out", 'w') as out:
    out.write(output + "\n")