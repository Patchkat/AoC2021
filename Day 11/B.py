map = []
for x in open("./input.txt").readlines():
    map.append([int(y) for y in x.rstrip()])
flashes = 0
step = 1
while True:
    for i, x in enumerate(map):
        for j, y in enumerate(map):
            map[i][j] += 1

    flashed = []
    old = -1
    while (old != len(flashed)):
        old = len(flashed)
        for i, x in enumerate(map):
            for j, _ in enumerate(x):
                if map[i][j] > 9 and (i,j) not in flashed:
                    flashes += 1
                    flashed.append((i,j))
                    for a in range(-1,2):
                        for b in range(-1,2):
                            c = a + i
                            d = b + j
                            if -1 < c < len(map) and -1 < d < len(x):
                                if a != 0 or b != 0:
                                    map[c][d] += 1
    for i, x in enumerate(map):
        for j, y in enumerate(map):
            if map[i][j] > 9:
                map[i][j] = 0
    
    num = 0
    for i, x in enumerate(map):
        for j, y in enumerate(map):
            if map[i][j] == 0:
                num += 1
    
    if num == len(map) * len(map[0]):
        break
    step += 1
print(step)