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

room = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,2,0,0,0,0],
        [0,0,0,0,2,2,2,0,0,0],
        [0,0,0,0,0,2,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]



# room = [[0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0]]


def is_finished():
    for r in range(len(room)):
        for c in range(len(room[r])):
            if (room[r][c] == 0):
                return False
    return True

print ("Started at coordinate " + str(x) + ", " + str(y))
room[y][x] = 1

while (not is_finished()):
    if (xDirection == "r"):
        if (x != len(room[y]) - 1 and room[y][x + 1] != 2):
            x = x + 1
            room[y][x] = 1;
            print("+Moved to coordinate " + str(x) + ", " + str(y))
        else:
            if (yDirection == "d"):
                if (y != len(room) - 1):
                    y = y + 1
                    room[y][x] = 1
                    xDirection = "l"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
                else:
                    yDirection = "u"
                    xDirection = "l"
                    y = y - 1
                    room[y][x] = 1
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
            else:
                if (y != 0):
                    y = y - 1
                    room[y][x] = 1
                    xDirection = "l"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
                else:
                    yDirection = "d"
                    xDirection = "l"
                    y = y + 1
                    room[y][x] = 1
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
                    y = y + 1
                    room[y][x] = 1
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
    else:
        if (x != 0  and room[y][x - 1] != 2):
            x = x - 1
            room[y][x] = 1;
            print("+Moved to coordinate " + str(x) + ", " + str(y))
        else:
            if (yDirection == "d"):
                if (y != len(room) - 1):
                    y = y + 1
                    room[y][x] = 1
                    xDirection = "r"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
                else:
                    yDirection = "u"
                    xDirection = "r"
                    y = y - 1
                    room[y][x] = 1
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
            else:
                if (y != 0):
                    y = y - 1
                    room[y][x] = 1
                    xDirection = "r"
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
                else:
                    yDirection = "d"
                    xDirection = "r"
                    y = y + 1
                    room[y][x] = 1
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
                    y = y + 1
                    room[y][x] = 1
                    print("+Moved to coordinate " + str(x) + ", " + str(y))
    print(room)
    time.sleep(0.1)
