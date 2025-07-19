# USACO 2021 February Contest Bronze #3: Clockwise Fence

N = int(input())

output = []

for i in range(N):
    fence = input()

    leftcount = 0
    rightcount = 0

    lastturn = fence[0]

    for element in fence[1:]:
        if element == 'W':
            if lastturn == 'N':
                leftcount += 1
            
            elif lastturn == 'S':
                rightcount += 1
            
        if element == 'E':
            if lastturn == 'N':
                rightcount += 1
            
            elif lastturn == 'S':
                leftcount += 1
        
        if element == 'N':
            if lastturn == 'E':
                leftcount += 1
            
            elif lastturn == 'W':
                rightcount += 1
        
        if element == 'S':
            if lastturn == 'E':
                rightcount += 1
            
            elif lastturn == 'W':
                leftcount += 1

        lastturn = element

    #print(leftcount, rightcount)
        
    if leftcount > rightcount:
        output.append("CCW")
    
    else:
        output.append("CW")

for i in range(len(output)):
    print(output[i])