# Zig zag
direction = "R"
returnToY = 0
avoidingUp = False
avoidingDown = False
x = 0
y = 0
room = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0]]

print ("Started at coordinate " + str(x) + ", " + str(y))

while (True):
        if (x == 0 and y == len(room) - 1):
            print("Completed Scan")
            break

        if (direction == "R"):
            #if the next coordinate is within bounds of the row
            if (x + 1 < len(room[1])):
                #if the next value is 1
                if(room[y][x+1] == 1):
                    #we found an obstalce
                    print("Found an obstacle")
                    #set the initial Y to the current Y
                    if (returnToY == 0):
                        returnToY = y
                    #if the obstacle is in the last row
                    if (y != len(room) - 1):
                        y = y + 1 #go below
                        #set avoidingDown to true so we move downwards
                        avoidingUp = False
                        avoidingDown = True

                    else:
                        #set avoidingUp to true so we move above the obstacle in last row
                        y = y - 1 #go above
                        avoidingUp = True
                        avoidingDown = False
                #if we are moving up or down and the obstacle is to our left and we have not made it back to Y
                elif ((avoidingUp or avoidingDown) and (y != returnToY)):
                    if(room[y-1][x] == 1 or room[y-1][x + 1] == 1):
                        x = x + 1
                    elif(room[y+1][x] == 1 or room[y+1][x + 1] == 1):
                        x = x + 1
                    # start to return to the old y row after avoiding obstacle
                    elif avoidingUp:
                        y = y + 1
                        print("here 1")
                    elif avoidingDown:
                        y = y - 1
                        print("here 2")
                    if (y == returnToY):
                        # this means we've navigated around the obstacle
                        avoidingUp = False
                        avoidingDown = False
                        returnToY = 0
                else:
                    x = x + 1
            else:
                y = y + 1
                direction = "L"

        elif (direction == "L"):
            if (x - 1 >= 0):
                if (room[y][x-1] == 1):
                    print("Found an obstacle")
                    #set the initial Y to the current Y
                    if (returnToY == 0):
                        returnToY = y
                    if (y != len(room) - 1):
                        y = y + 1 #go below
                        avoidingUp = False
                        avoidingDown = True

                    else:
                        y = y - 1 #go above
                        avoidingUp = True
                        avoidingDown = False
                                #if we are moving up or down and the obstacle is to our left and we have not made it back to Y
                elif ((avoidingUp or avoidingDown) and (y != returnToY)):
                    if(room[y-1][x-1] == 1 or room[y-1][x] == 1):
                        x = x - 1
                    elif(room[y+1][x] == 1 or room[y+1][x - 1] == 1):
                        x = x - 1
                    # start to return to the old y row after avoiding obstacle
                    elif avoidingUp:
                        y = y + 1
                        print("here 3")
                    elif avoidingDown:
                        y = y - 1
                        print("here 4")
                    if (y == returnToY):
                        # this means we've navigated around the obstacle
                        avoidingUp = False
                        avoidingDown = False
                        returnToY = 0
                else:
                    x = x - 1
            else:
                y = y + 1
                direction = "R"

        print("Avoiding Up: " + str(avoidingUp))
        print("Avoiding Down: " + str(avoidingDown))
        print("Return to Y: " + str(returnToY))
        print("Moved to coordinate " + str(x) + ", " + str(y))
