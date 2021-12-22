wronglines = []
score = 0
for x in open("./input.txt").readlines():
    x = x.rstrip()
    stack = []
    for y in x:
        if y in ["<", "[", "{", "("]:
            stack.append(y)
        else:
            open = stack.pop()
            if open == "<" and y != ">":
                if y == ")":
                    score += 3
                elif y == "}":
                    score += 1197
                else:
                    score += 57
                break
            elif open == "(" and y != ")":
                if y == ">":
                    score += 25137
                elif y == "}":
                    score += 1197
                else:
                    score += 57
                break
            elif open == "{" and y != "}":
                if y == ">":
                    score += 25137
                elif y == ")":
                    score += 3
                else:
                    score += 57
                break
            elif open == "[" and y != "]":
                if y == ")":
                    score += 3
                elif y == "}":
                    score += 1197
                else:
                    score += 25137
                break
print(score)