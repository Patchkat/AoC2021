def make_path(map):
    big_value = 1000000
    tc = [[big_value for _ in range(len(map))] for _ in range(len(map))]

    tc[0][0] = 0

    for i in range(1, len(map)):
        tc[i][0] = tc[i-1][0] + map[i][0]
    
    for i in range(1, len(map)):
        tc[0][i] = tc[0][i-1] + map[0][i]

    curr_cost = big_value
    prev_cost = big_value+1
    while prev_cost > curr_cost:
        prev_cost = curr_cost
        for i in range(1, len(map)):
            for j in range(1, len(map)):
                temp_min = min(tc[i-1][j], tc[i][j-1])
                other_min = big_value
                if j < len(map)-1:
                    other_min = tc[i][j+1]
                if i < len(map)-1:
                    other_min = min(other_min, tc[i+1][j])
                tc[i][j] = min(temp_min, other_min) + map[i][j]
        curr_cost = tc[-1][-1]
    return tc
    
    

map = []
j = 0
for x in open("./input.txt").readlines():
    map.append([])
    for y in x.rstrip():
        map[j].append(int(y))
    j += 1

cost = make_path(map)    
print(cost[-1][-1]-2)