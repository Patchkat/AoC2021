size = 991
points = [[0 for x in range(size)] for y in range(size)]
for x in open("./vents.txt").readlines():
    y = x.rstrip().split(" -> ")
    x1, y1 = [int(x) for x in y[0].split(",")]
    x2, y2 = [int(x) for x in y[1].split(",")]
    if x1 == x2:
        if y1 > y2:
            while y2 <= y1:
                points[x1][y2] += 1
                y2 += 1
        else:
            while y1 <= y2:
                points[x1][y1] += 1
                y1 += 1
    elif y1 == y2:
        if x1 > x2:
            while x2 <= x1:
                points[x1][y1] += 1
                x1 -= 1
        else:
            while x1 <= x2:
                points[x1][y1] += 1
                x1 += 1
    elif x1 > x2 and y1 > y2:
        while x1 >= x2 and y1 >= y2:
            points[x1][y1] += 1
            x1 -= 1
            y1 -= 1
    elif x1 < x2 and y1 < y2:
        while x1 <= x2 and y1 <= y2:
            points[x1][y1] += 1
            x1 += 1
            y1 += 1
    elif x1 < x2 and y1 > y2:
        while x1 <= x2 and y1 >= y2:
            points[x1][y1] += 1
            x1 += 1
            y1 -= 1
    else:
        while x1 >= x2 and y1 <= y2:
            points[x1][y1] += 1
            x1 -= 1
            y1 += 1

total = 0
for x in points:
    for y in x:
        if y >= 2:
            total += 1
    # print(x)
print(total)