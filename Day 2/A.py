pos = 0
dep = 0
for x in open("./directions.txt").readlines():
    x = x.split(" ")
    if x[0].startswith("f"):
        pos += int(x[1])
    elif x[0].startswith("u"):
        dep -= int(x[1])
    elif x[0].startswith("d"):
        dep += int(x[1])
print(pos * dep)
