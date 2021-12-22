pairs = {}
code = []
codebool = True
for x in open("./input.txt").readlines():
    if x == "\n":
        codebool = False
        continue
    x = x.rstrip()
    if codebool:
        for z in range(len(x)-1):
            code.append([x[z], x[z+1]])
    else:
        z = x.split(" -> ")
        pairs[z[0]] = z[1]
for _ in range(10):
    new_code = []
    for c in code:
        b = ''.join(c)
        if b in pairs.keys():
            new_code.append([c[0], pairs[b]])
            new_code.append([pairs[b], c[1]])
    code = new_code

scode = ''.join([x[0] for x in code])
scode += code[-1][1]
counts = []
letters = set(pairs.values())
for x in letters:
    counts.append(scode.count(x))
print(max(counts) - min(counts))