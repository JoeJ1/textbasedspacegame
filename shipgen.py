import random


def generateRoom(width, height, shipLength):  # width and height refer to the size of the array within which the ship will be drawn and the shipLength refer to how many rooms are created by the function
    shipArray = []                            # The program continues to make the level to the size of shiplength unless it creates it in an impossible way, in which case it is cut short.
    for i in range(height):
        shipArray.append([0]*width)
    x = 0
    y = 0
    shipArray[0][0] = 1
    for i in range(shipLength):
        if(len(directionsCheck(x, y, shipArray)) != 0):
            direction = random.choice(directionsCheck(x, y, shipArray))
            if(direction == "up"):
                y = y - 1
            elif(direction == "down"):
                y = y + 1
            elif(direction == "left"):
                x = x - 1
            elif(direction == "right"):
                x = x + 1
            shipArray[y][x] = 1
        else:
            shipArray[y][x] = 2
            break
        if(i == shipLength-1):
            shipArray[y][x] = 2
    return(shipArray)


def cleanArray(array):  # Removes any elements of an array if they are just an empty string.
    i = 0
    while(i < len(array)):  # Don't change this to a for loop, it needs to be a while so I can reset "i" to zero to reiterate through the array. This is neccisary as if an element is removed the array gets shorter so may skip over some elements.
        if(array[i] == ""):
            del array[i]
            i = 0
        i = i + 1
    return(array)


def directionsCheck(x, y, shipArray):
    directions = ["right", "left", "up", "down"]
    if(x >= len(shipArray[y])):
        directions[0] = ""
    if(x <= 0):
        directions[1] = ""
    if(y <= 0):
        directions[2] = ""
    if(y >= len(shipArray)):
        directions[3] = ""

    if(directions[0] != ""):  # Needs to be nested if statements otherwise python gets all sad if it y+/-1 or x+/-1 is out of range.
        try:
            if(shipArray[y][x+1] == 1):
                directions[0] = ""
        except:
            directions[0] = ""
    if(directions[1] != ""):
        try:
            if(shipArray[y][x-1] == 1):
                directions[1] = ""
        except:
            directions[1] = ""
    if(directions[2] != ""):
        try:
            if(shipArray[y-1][x] == 1):
                directions[2] = ""
        except:
            directions[2] = ""
    if(directions[3] != ""):
        try:
            if(shipArray[y+1][x] == 1):
                directions[3] = ""
        except:
            directions[3] = ""
    return(cleanArray(directions))

# uncomment below for quick testing.
# for k in range(10):
#     room = generateRoom(10, 10, 100)
#     print("\n"*3+"iteration: {}".format(k))
#     for i in range(len(room)):
#         for j in range(len(room[i])):
#             room[i][j] = str(room[i][j]).replace("0", "░")
#             room[i][j] = str(room[i][j]).replace("1", "█")
#             room[i][j] = str(room[i][j]).replace("2", "▒")
#         print(''.join(room[i]))
