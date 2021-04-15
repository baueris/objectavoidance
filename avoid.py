# Zig zag
direction = "r"
avoidDirection = "d"
x = 0
y = 0

avoiding = False

room = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,2,2,2,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

# room = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0],
#         [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0]]

print ("Started at coordinate " + str(x) + ", " + str(y))
room[y][x] = 1

while (True):
    if(not avoiding):
        if (direction == "r"):
            if (x != len(room[1]) - 1):
                if (room[y][x + 1] != 2):
                    x = x + 1
                    room[y][x] = 1;
                    print("Moved to coordinate " + str(x) + ", " + str(y))
                    continue
                else:
                    avoiding = True
                    avoidDirection = "d"
                    returnToY = y
                    print("Found an obstacle")
                    continue
            else:
                if (y != len(room) - 1):
                    y = y + 1
                    direction = "l"
                    room[y][x] = 1;
                    print("Moved to coordinate " + str(x) + ", " + str(y))
                    continue
                else:
                    print("Scan completed")
                    break
        else:
            if (x != 0):
                if (room[y][x - 1] != 2):
                    x = x - 1
                    room[y][x] = 1;
                    print("Moved to coordinate " + str(x) + ", " + str(y))
                    continue
                else:
                    avoiding = True
                    returnToY = y
                    avoidDirection = "d"
                    print("Found an obstacle")
                    continue
            else:
                if (y != len(room) - 1):
                    y = y + 1
                    direction = "r"
                    room[y][x] = 1;
                    print("Moved to coordinate " + str(x) + ", " + str(y))
                    continue
                else:
                    print("Scan completed")
                    break
    else:
        # Avoiding
        if (avoidDirection == "d"):
            if (y != len(room) - 1 and room[y - 1][x] != "2"):
                y = y + 1
                print("*Moved to coordinate " + str(x) + ", " + str(y)) # "*" means avoiding
            elif (room[y - 1][x] != "2"):
                avoidDirection = "u"
                y = y + 1
                print("*Moved to coordinate " + str(x) + ", " + str(y))
                continue
            elif (direction == "l"):
                avoidDirection = "r"
                continue
            else:
                avoidDirection = "l"
                continue
            # Test if can navigate obstacle after moving down 1
            if (direction == "r"):
                if (x != len(room[1]) - 1 and room[y][x + 1] != "2"):
                    x = x + 1;
                    print("*Moved to coordinate " + str(x) + ", " + str(y))
            else:
                if (x != 0 and room[y][x - 1] != "2"):
                    x = x - 1;
                    print("*Moved to coordinate " + str(x) + ", " + str(y))

print(room)
