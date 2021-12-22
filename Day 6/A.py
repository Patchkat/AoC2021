for x in open("./fish.txt").readlines():
    fish = [int(y) for y in x.split(",")]
time = 0
while time < 80:
    for i, x in enumerate(fish):
        if x != 0:
            fish[i] = fish[i] - 1
        else:
            fish[i] = 6
            fish.append(9)
    time += 1
print(len(fish))