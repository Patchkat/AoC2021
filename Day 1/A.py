total = 0
values = []
for x in open("./depth.txt").readlines():
    values.append(int(x))

for i in range(len(values)):
    if i != 0:
        if values[i] > values[i-1]:
            total += 1
print(total)
