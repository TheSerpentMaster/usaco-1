# USACO 2023 February Contest Bronze #3 Moo Operations

Q = int(input())

output = []

for idx in range(Q):
    text = input()

    if "MOO" in text:
        output.append(len(text) - 3)
        continue

    if len(text) == 3:
        total = 0

        if text[1] == 'M':
            output.append(-1)
            continue

        if text[0] != "M":
            total += 1
        
        if text[2] != 'O':
            total += 1
        
        output.append(total)
        continue
    
    minimum = len(text)
    already_passed = set([])
    
    for start in range(len(text) - 2):
        end = start + 3
        #print(start, end)

        segment = text[start:end]
        #print(segment)

        if segment in already_passed:
            continue

        if segment[1] == 'M':
            continue
        else:
            total = 0
            if segment[0] != "M":
                total += 1
            if segment[2] != 'O':
                total += 1
            total += (len(text) - 3)
            if total < minimum:
                minimum = total
        
        already_passed.add(segment)

    if minimum == len(text):
        output.append(-1)
        continue
    
    output.append(minimum)

for i in range(len(output)):
    print(output[i])