from os import truncate


outputs = []
inputs = []
for x in open('./signals.txt').readlines():
    line = x.rstrip("\n").split("|")
    inputs += [line[0].strip().split(" ")]
    outputs += [line[1].strip().split(" ")]
total = 0
for i, x in enumerate(inputs):
    rspots = {}
    numbers = {0 : [], 5: []}
    newnumbers = {0 : "", 1 : "", 2 : "", 3 : "", 4 : "", 5 : "", 6 : "", 7 : "", 8 : "", 9 : ""}

    # Get the easy numbers set, and store the rest
    for y in x:
        if len(y) == 2:
            newnumbers[1] = y
        elif len(y) == 4:
            newnumbers[4] = y
        elif len(y) == 3:
            newnumbers[7] = y
        elif len(y) == 7:
            newnumbers[8] = y
        elif len(y) == 6:
            numbers[0].append(y)
        elif len(y) == 5:
            numbers[5].append(y)

    # Figure out which number is which
    for y in numbers[0]:
        if len([z for z in y if z not in [z for z in newnumbers[4] if z not in newnumbers[1]]]) == 5:
            newnumbers[0] = y
        elif len([z for z in y if z not in newnumbers[7]]) == 4:
            newnumbers[6] = y
        else:
            newnumbers[9] = y
    for y in numbers[5]:
        if len([z for z in y if z not in newnumbers[6]]) == 0:
            newnumbers[5] = y
        elif len([z for z in y if z not in newnumbers[1]]) == 3:
            newnumbers[3] = y
        else:
            newnumbers[2] = y

    # Start figuring out letters
    for letter in newnumbers[7]:
        if letter not in newnumbers[1]:
            rspots[letter] = "a"
    rspots[[z for z in newnumbers[5] if z not in newnumbers[3]][0]] = "b"
    rspots[[z for z in newnumbers[7] if z not in newnumbers[6]][0]] = "c"
    four = [z for z in newnumbers[4] if z not in newnumbers[1]]
    rspots[[z for z in four if z not in rspots.keys()][0]] = "d"
    six = [z for z in newnumbers[6] if z not in newnumbers[3]]
    rspots[[z for z in six if z not in rspots.keys()][0]] = "e"
    rspots[[z for z in newnumbers[1] if z not in rspots.keys()][0]] = "f"
    rspots[[z for z in newnumbers[9] if z not in rspots.keys()][0]] = "g"

    number = ""
    for y in outputs[i]:
        correct = ""
        for z in y:
            correct += rspots[z]
        if len(correct) == 2:
            number += "1"
        elif len(correct) == 3:
            number += "7"
        elif len(correct) == 4:
            number += "4"
        elif len(correct) == 5:
            if set(correct) == set(["a", "c", "d", "e", "g"]):
               number += "2"
            elif set(correct) == set(["a", "c", "d", "f", "g"]):
                number += "3"
            else:
                number += "5"
        elif len(correct) == 6:
            if set(correct) == set(["a", "b", "d", "e", "f", "g"]):
               number += "6"
            elif set(correct) == set(["a", "b", "c", "f", "e", "g"]):
               number += "0"
            else:
                number += "9"
        elif len(correct) == 7:
            number += "8"
    total += int(number)
print(total)