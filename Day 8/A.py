outputs = []
for x in open('./signals.txt').readlines():
    output = x.rstrip("\n").split("|")[1]
    outputs += output.strip().split(" ")
total = 0
for s in outputs:
    if len(s) in [2, 3, 7, 4]:
        total += 1 
print(total)