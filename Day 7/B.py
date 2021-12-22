nums = []
for x in open("./crabs.txt").readlines():
    nums = [int(y) for y in x.rstrip("\n").split(",")]
max = max(nums)
min = min(nums)
maxfuel = max * len(nums) * max
num = 0
for x in range(min, max+1):
    fuel = 0
    for y in nums:
        if y > x:
            step = 1
            while y > x:
                y -= 1
                fuel += step
                step += 1
        else:
            step = 1
            while y < x:
                y += 1
                fuel += step
                step += 1
    if fuel < maxfuel:
        maxfuel = fuel
        num = x

print(num)
print(maxfuel)