nums = [0 for x in range(12)]
fnums = []
total = 0
for x in open("./diagnostic.txt").readlines():
    for i, y in enumerate(x):
        if y == "1":
            nums[i] += 1
    total += 1
for x in nums:
    if x > total/2:
        fnums.append("1")
    else:
        fnums.append("0")
gamma = ''.join(fnums)
epsilon = ''.join(["1" if x == "0" else "0" for x in fnums])

print(int(epsilon, 2) * int(gamma, 2))