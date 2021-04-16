# Zig zag
#
import time

xDirection = "r"
yDirection = "d"
x = 0
y = 0
returnToY = 0
originalX = 0

avoiding = False

# lines
room = [[".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".","X","X","X",".",".",".","."],
        [".",".","X","X","X","X","X",".",".","."],
        [".",".","X","X","X","X","X",".",".","."],
        [".",".","X","X","X","X","X",".",".","."],
        [".",".",".","X","X","X",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."]]


def is_finished():
    finished = True
    for r in range(len(room)):
        for c in range(len(room[r])):
            if (room[r][c] == "."):
                finished = False
            if (room[r][c] == "*"):
                room[r][c] = "o"
    return finished

print ("Started at coordinate " + str(x) + ", " + str(y))
room[y][x] = "o"

while (not is_finished()):
    if (xDirection == "r"):
        if (x != len(room[y]) - 1 and room[y][x + 1] != "X"):
            x = x + 1
            room[y][x] = "*"
            print("+Moved to coordinate " + str(x) + ", " + str(y))
        else:
            if (yDirection == "d"):
                if (y != len(room) - 1 and room[y + 1][x] != "X"):
                    y = y + 1
                    room[y][x] = "*"
                    xDirection = "l"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
                elif (y == len(room) - 1):
                    # last row
                    yDirection = "u"
                    xDirection = "l"
                    y = y - 1
                    room[y][x] = "*"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
                else:
                    while (room[y+1][x] == "X"):
                        x = x - 1
                    y = y + 1
                    room[y][x] = "*"
                    xDirection = "l"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))

            else:
                if (y != 0 and room[y - 1][x] != "X"):
                    y = y - 1
                    room[y][x] = "*"
                    xDirection = "l"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
                elif (room[y - 1][x] != "X"):
                    yDirection = "d"
                    xDirection = "l"
                    y = y + 1
                    room[y][x] = "*"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
                    y = y + 1
                    room[y][x] = "*"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
                else:
                    while (room[y+1][x] == "X"):
                        x = x + 1
                    y = y + 1
                    room[y][x] = "*"
                    xDirection = "l"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
    else:
        # moving left
        if (x != 0  and room[y][x - 1] != "X"):
            x = x - 1
            room[y][x] = "*";
            print("+Moved to coordinate " + str(x) + ", " + str(y))
        else:
            if (yDirection == "d"):
                if (y != len(room) - 1 and room[y + 1][x] != "X"):
                    #normal row
                    y = y + 1
                    room[y][x] = "*"
                    xDirection = "r"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
                elif (y == len(room) - 1):
                    # last row
                    yDirection = "u"
                    xDirection = "r"
                    y = y - 1
                    room[y][x] = "*"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
                else:
                    # blocking row
                    while (room[y+1][x] == "X"):
                        x = x + 1
                    y = y + 1
                    room[y][x] = "*"
                    xDirection = "r"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
            else:
                if (y != 0 and room[y - 1][x] != "X"):
                    y = y - 1
                    room[y][x] = "*"
                    xDirection = "r"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
                elif (room[y - 1][x] != "X"):
                    yDirection = "d"
                    xDirection = "r"
                    y = y + 1
                    room[y][x] = "*"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
                else:
                    while (room[y+1][x] == "X"):
                        x = x + 1
                    y = y + 1
                    room[y][x] = "*"
                    xDirection = "r"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
    print(room)
    time.sleep(0.1)
