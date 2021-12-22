def create_string(scode, pairs):
    rcode = scode[0]
    print(len(scode))
    for x in range(len(scode)-1):
        b = ''.join([scode[x], scode[x+1]])
        if b in pairs.keys():
            rcode += pairs[b] + b[1]
    return rcode


pairs = {}
code = ""
codebool = True
for x in open("./input.txt").readlines():
    if x == "\n":
        codebool = False
        continue
    x = x.rstrip()
    if codebool:
        for z in range(len(x)):
            code += x[z]
    else:
        z = x.split(" -> ")
        pairs[z[0]] = z[1]

counts = {}
temp_counts = {}
big_counts = {}
prev_counts = {}
prev_big = {}
letters = set(pairs.values())
for x in letters:
    counts[x] = 0
counts[code[-1]] = 1
for x in range(len(code)-1):
    for l in letters:
        big_counts[l] = counts[l]
    tcode = ''.join([code[x], code[x+1]])
    jcode = tcode
    if tcode in prev_big.keys():
        for z in letters:
            counts[z] += prev_big[tcode][z]
        continue
    for y in range(20):
        tcode = create_string(tcode, pairs)
    for y in range(len(tcode)-1):
        ucode = ''.join([tcode[y], tcode[y+1]])
        icode = ucode
        if ucode in prev_counts.keys():
            for z in letters:
                counts[z] += prev_counts[ucode][z]
            continue
        for z in range(20):
            ucode = create_string(ucode, pairs)
        ucode = ucode[:-1]
        for z in letters:
            lcount = ucode.count(z)
            temp_counts[z] = lcount
            counts[z] += lcount
        prev_counts[icode] = dict(temp_counts)
    for z in letters:
        big_counts[z] = counts[z] - big_counts[z]
    prev_big[jcode] = dict(big_counts)
    

print(max(counts.values()) - min(counts.values()))