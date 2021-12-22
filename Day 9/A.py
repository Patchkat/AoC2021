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
                            lowpoints.append(y)
            elif i > 0:
                if map[i-1][j-1] > y and map[i-1][j] > y and map[i-1][j+1]:
                    if map[i][j-1] > y and map[i][j+1] > y:
                        lowpoints.append(y)
            else:
                if map[i][j-1] > y and map[i][j+1]:
                    if map[i+1][j-1] > y and map[i+1][j] > y and map[i][j+1] > y:
                        lowpoints.append(y)
        elif j > 0:
            if len(map) - 1 > i > 0:
                if map[i-1][j-1] > y and map[i-1][j] > y:
                    if map[i][j-1] > y:
                        if map[i+1][j-1] > y and map[i+1][j] > y:
                            lowpoints.append(y)
            elif i > 0:
                if map[i-1][j-1] > y and map[i-1][j] > y:
                    if map[i][j-1] > y:
                        lowpoints.append(y)
            else:
                if map[i][j-1] > y:
                    if map[i+1][j-1] > y and map[i+1][j] > y:
                        lowpoints.append(y)
        else:
            if len(map) - 1 > i > 0:
                if map[i-1][j] > y and map[i-1][j+1]:
                    if map[i][j+1] > y:
                        if map[i+1][j] > y and map[i+1][j+1] > y:
                            lowpoints.append(y)
            elif i > 0:
                if map[i-1][j] > y and map[i-1][j+1]:
                    if map[i][j+1] > y:
                        lowpoints.append(y)
            else:
                if map[i][j+1]:
                    if map[i+1][j] > y and map[i][j+1] > y:
                        lowpoints.append(y)
print(sum([x+1 for x in lowpoints]))
