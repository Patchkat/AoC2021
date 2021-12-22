incompletelines = []
scores = []
for x in open("./input.txt").readlines():
    score = 0
    x = x.rstrip()
    stack = []
    broken = False
    for y in x:
        if y in ["<", "[", "{", "("]:
            stack.append(y)
        else:
            open = stack.pop()
            if open == "<" and y != ">":
                broken = True
                break
            elif open == "(" and y != ")":
                broken = True
                break
            elif open == "{" and y != "}":
                broken = True
                break
            elif open == "[" and y != "]":
                broken = True 
                break
    if not broken:
        for z in stack[::-1]:
            if z == "<":
                score *= 5
                score += 4
            elif z == "(":
                score *= 5
                score += 1
            elif z == "{":
                score *= 5
                score += 3
            elif z == "[":
                score *= 5
                score += 2
    if score != 0:
        scores.append(score)
print(sorted(set(scores))[int(len(scores)/2)])