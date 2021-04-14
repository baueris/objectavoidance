# Zig zag
direction = "R"
returnToY = 0
avoidingUp = False
avoindingDown = False
x = 0
y = 0
room = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

print ("Started at coordinate " + str(x) + ", " + str(y))

while (True):
        if (x == len(room[0]) - 1 and y == len(room) - 1):
            print("Completed Scan")
            break

        if (direction == "R"):
            if (x + 1 < len(room[1])):
                if (room[y][x+1] == 1):
                    print("Found an obstacle")
                    returnToY = y
                    if (y != len(room) - 1):
                        y = y + 1 #go below
                        avoidingUp = False
                        avoidingDown = True

                    else:
                        y = y - 1 #go above
                        avoidingUp = True
                        avoidingDown = False
                elif (avoidingUp or avoidingDown and (room[y][x-1] == 1 and y != returnToY)):
                    # start to return to the old y row after avoiding obstacle
                    if avoidingUp:
                        y = y + 1
                    else
                        y = y - 1
                    if (y == returnToY)
                        # this means we've navigated around the obstacle
                        avoidingUp = False
                        avoidingDown = False
                else:
                    x = x + 1
            else:
                y = y + 1
                direction = "L"

        elif (direction == "L"):
            if (x - 1 >= 0):
                if (room[y][x-1] == 1):
                    print("Found an obstacle")
                    returnToY = y
                    if (y != len(room) - 1):
                        y = y + 1 #go below
                        avoidingUp = False
                        avoidingDown = True

                    else:
                        y = y - 1 #go above
                        avoidingUp = True
                        avoidingDown = False
                else:
                    x = x - 1
            else:
                y = y + 1
                direction = "R"
        print ("Moved to coordinate " + str(x) + ", " + str(y))
