pos = 0
dep = 0
aim = 0
for x in open("./directions.txt").readlines():
    x = x.split(" ")
    if x[0].startswith("f"):
        pos += int(x[1])
        dep += aim * int(x[1])
    elif x[0].startswith("u"):
        aim -= int(x[1])
    elif x[0].startswith("d"):
        aim += int(x[1])
print(pos * dep)