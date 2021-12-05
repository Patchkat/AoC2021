def check_board(board):
    for x in board:
        if x == ["-1", "-1", "-1", "-1", "-1"]:
            return True
    done = True
    for i in range(5):
        for x in board:
            if x[i] != "-1":
                done = False
                break
        if done:
            return True
        done = True
    return False

def calculate_values(board):
    total = 0
    for x in board:
        for y in x:
            if y != "-1":
                total += int(y)
    return total
            

boards = {}
x = open("./bingo.txt")

nums = x.readline().split(",")
x.readline()
board = []
num = 0
for y in x.readlines():
    if y != "\n":
        board.append(y.strip("\n").split())
    else:
        boards[num] = board
        num += 1
        board = []
boards[num] = board
done = False
for x in nums:
    for key in boards.keys():
        board = boards[key]
        for i, line in enumerate(board):
            if x in line:
                j = line.index(x)
                board[i][j] = "-1"
                if check_board(board):
                    done = True
                    break
                boards[key] = board
        if done:
            break
    if done:
        total = calculate_values(board)
        print(total * int(x))
        break

