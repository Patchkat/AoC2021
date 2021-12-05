total = 0
values = []
for x in open("./depth.txt").readlines():
    values.append(int(x))

prevsum = values[0] + values[1] + values[2]
for i in range(len(values)):
    if i < len(values) - 2:
        sum = values[i] + values[i+1] + values[i+2]
        if sum > prevsum:
            total += 1
        prevsum = values[i] + values[i+1] + values[i+2]


print(total)
