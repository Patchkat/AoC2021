for x in open("./fish.txt").readlines():
    fish = [int(y) for y in x.split(",")]
fish_count = [0 for x in range(9)]
day = 0
for x in fish:
    fish_count[x] += 1
while day < 256:
    new_fish = fish_count[0]
    for x in range(1, 9):
        fish_count[x-1] = fish_count[x]
    fish_count[8] = new_fish
    fish_count[6] += new_fish
    day += 1
print(sum(fish_count))