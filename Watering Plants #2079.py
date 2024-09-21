plants = [2,2,3,3]
capacity = 8
steps = 0
for i in range(0,len(plants)):
    if capacity >= plants[i]:
        print(capacity,"cap")
        steps += 1
        print(steps,"inloop")
    else:
        steps += (2*i)+1    #walk back to river +1 water new plant
        capacity = 8    
        print(steps,"else")
    capacity -= plants[i]

print(steps)