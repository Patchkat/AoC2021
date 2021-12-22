map = []
for x in open("./signals.txt").readlines():
    map.append([int(y) for y in x.rstrip()])
lowpoints = []
for i, x in enumerate(map):
    for j, y in enumerate(x):
        if len(x) - 1 > j > 0:
            if len(map) - 1 > i > 0:
                if map[i-1][j-1] > y and map[i-1][j] > y and map[i-1][j+1]:
                    if map[i][j-1] > y and map[i][j+1] > y:
                        if map[i+1][j-1] > y and map[i+1][j] > y and map[i+1][j+1] > y:
                            lowpoints.append((i, j))
            elif i > 0:
                if map[i-1][j-1] > y and map[i-1][j] > y and map[i-1][j+1]:
                    if map[i][j-1] > y and map[i][j+1] > y:
                        lowpoints.append((i,j))
            else:
                if map[i][j-1] > y and map[i][j+1]:
                    if map[i+1][j-1] > y and map[i+1][j] > y and map[i][j+1] > y:
                        lowpoints.append((i, j))
        elif j > 0:
            if len(map) - 1 > i > 0:
                if map[i-1][j-1] > y and map[i-1][j] > y:
                    if map[i][j-1] > y:
                        if map[i+1][j-1] > y and map[i+1][j] > y:
                            lowpoints.append((i, j))
            elif i > 0:
                if map[i-1][j-1] > y and map[i-1][j] > y:
                    if map[i][j-1] > y:
                        lowpoints.append((i, j))
            else:
                if map[i][j-1] > y:
                    if map[i+1][j-1] > y and map[i+1][j] > y:
                        lowpoints.append((i, j))
        else:
            if len(map) - 1 > i > 0:
                if map[i-1][j] > y and map[i-1][j+1]:
                    if map[i][j+1] > y:
                        if map[i+1][j] > y and map[i+1][j+1] > y:
                            lowpoints.append((i, j))
            elif i > 0:
                if map[i-1][j] > y and map[i-1][j+1]:
                    if map[i][j+1] > y:
                        lowpoints.append((i, j))
            else:
                if map[i][j+1]:
                    if map[i+1][j] > y and map[i][j+1] > y:
                        lowpoints.append((i, j))

basin_size = []
basin_points = []
for x in lowpoints:
    new_points = [x]
    pos = 0
    basin = True
    while(basin):
        point = new_points[pos]
        val = map[point[0]][point[1]]
        c = point[0]
        if -1 < c < len(map):
            d = point[1] - 1
            if -1 < d < len(map[0]):
                if map[c][d] > val and map[c][d] != 9 and new_points.count((c,d)) == 0 and basin_points.count((c,d)) == 0:
                    new_points.append((c,d))
        c = point[0] - 1
        if -1 < c < len(map):
            d = point[1]
            if -1 < d < len(map[0]):
                if map[c][d]> val and map[c][d] != 9 and new_points.count((c,d)) == 0 and basin_points.count((c,d)) == 0:
                    new_points.append((c,d))
        c = point[0] + 1
        if -1 < c < len(map):
            d = point[1]
            if -1 < d < len(map[0]):
                if map[c][d] > val and map[c][d] != 9 and new_points.count((c,d)) == 0 and basin_points.count((c,d)) == 0:
                    new_points.append((c,d))
        c = point[0]
        if -1 < c < len(map):
            d = point[1] + 1
            if -1 < d < len(map[0]):
                if map[c][d] > val and map[c][d] != 9 and new_points.count((c,d)) == 0 and basin_points.count((c,d)) == 0:
                    new_points.append((c,d))
        pos += 1
        if (len(new_points) == pos):
            basin = False
    basin_size.append(len(new_points))
    for l in new_points:
        basin_points.append(l)
prod = sorted(basin_size)
print(prod.pop() * prod.pop() * prod.pop()) 
        
    
    