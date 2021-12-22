def rotateArray(A):
    N = [[0 for x in range(len(A))] for z in range(len(A[0]))]
    for i, a in enumerate(A):
        for j, b in enumerate(a):
            N[j][len(A)-1-i] = b
    return N
        
            


instr = []
max_x = 0
max_y = 0
for x in open("./input.txt").readlines():
    if x == "\n":
        break
    d = [int(z) for z in x.rstrip().split(",")]
    if d[0] > max_y:
        max_y = d[0]
    if d[1] > max_x:
        max_x = d[1]

dots = [["." for x in range(max_y+1)] for z in range(max_x+1)]
dot = True
for x in open("./input.txt").readlines():
    if x == "\n":
        dot = False
        continue
    if dot:
        d = [int(z) for z in x.rstrip().split(",")]
        dots[d[1]][d[0]] = "#"
    else:
        z = x.rstrip().split(" ")[2].split("=")
        instr.append((z[0], int(z[1])))
for t in instr:
    x = t[0]
    y = t[1]
    if x == "y":
        dots.reverse()
        c = [d for d in dots[:y]]
        dots.reverse()
        for i, z in enumerate(c):
            for j, a in enumerate(z):
                if a == "#":
                    dots[i][j] = "#"
        dots = dots[:y]
    else:
        dots = rotateArray(dots)
        dots.reverse()
        c = [d for d in dots[:y]]
        dots.reverse()
        for i, z in enumerate(c):
            for j, a in enumerate(z):
                if a == "#":
                    dots[i][j] = "#"
        dots = dots[:y]
        dots = rotateArray(dots)
        dots = rotateArray(dots)
        dots = rotateArray(dots)
total = 0
for x in dots:
    print(x)
print(total)