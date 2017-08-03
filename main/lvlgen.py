import random
import var


def listtostring(lst):  # Converts a list into a string without the special charachters of a list (brackets and commas etc.)
    lst = str(lst)
    lst = lst.replace("\"", "")
    lst = lst.replace("\"", "")
    lst = lst.replace("'", "")
    lst = lst.replace(",", "")
    lst = lst.replace("]", "")
    lst = lst.replace("[", "")
    lst = lst.replace(" ", "")
    return(lst)


def shipgen(size, length):
    # array = ["", ]*sizey*sizex
    # i = 0
    # while(i < len(array)):
    #     randomint = random.randint(0, 99)
    #     if(randomint < 50):
    #         array[i] = 0
    #     elif(randomint >= 50 and randomint < 90):
    #         array[i] = random.randint(1, 7)
    #     elif(randomint >= 90 and randomint < 100):
    #         array[i] = random.randint(8, 9)
    #     i = i+1
    # array[0] = 1
    # string = ','.join(str(array))
    # string = string.replace("[", "")
    # string = string.replace("]", "")
    # string = string.replace(",", "")
    # string = string.replace(" ", "")
    # string = [string[a:a+sizey] for a in range(0, len(string), sizey)]
    # return(string)
    #############################################################################################################
    # Invert above comment to use random noise generation for level generation instead of random path generation.#
    #############################################################################################################

    area = ["0"*size]*size  # making the level
    choices = [""]*length  # creating the list of direction choices
    x = 0  # defining positional variables for the current position of the "path drawer" (drawer as in one who draws not cupboard)
    y = 0  # ""
    i = 0  # i is a placeholder for the current point in the list. Used to increment through a list and change each element.
    while(i < length):
        options = ["right", "left", "up", "down"]  # Creating a list of all possible directions then removing them if the path cannot go in that direction
        if(x == 0):  # checking if the path drawer is at the left wall,
            options.remove("left")  # if so removing the option to move left.
        if(x == len(area[y])-1):  # checking if the path drawer is at the right wall,
            options.remove("right")  # if so removing the option to move right.
        if(y == len(area)-1):  # checking if the path drawer is at the bottom wall,
            options.remove("down")  # if so removing the option to move down.
        if(y == 0):  # checking to see if the path drawer is at the top wall,
            options.remove("up")  # if so removing the option to move up.
        if(len(options) == 0):  # checking if any direction can be moved in,
            break  # if not then stop incrementing
        direction = options[random.randint(0, len(options)-1)]  # randomly choosing which direction to move in from the list of possible directions
        choices[i] = direction  # adding it to the list of direction choices
        i = i + 1  # incrementing
    i = 0  # reseting "i" to reuse for another while loop
    while(i < len(choices)):  # incrementing the list of choices
        if(choices[i] == "left"):  # checking to see which direction to move in
            x = x - 1  # moveing in that direction
        elif(choices[i] == "right"):  # ""
            x = x + 1  # ""
        elif(choices[i] == "up"):  # ""
            y = y - 1  # ""
        elif(choices[i] == "down"):  # ""
            y = y + 1  # ""
        currentln = list(area[y])  # converting the list of x coordinates into x and y
        currentln[x] = "1"  # making the current position 1 (a pathway)
        area[y] = listtostring(currentln)  # adding that position to the list/area
        i = i + 1  # incrementing "i"
    currentln = list(area[y])  # making the last point in the path 2 (a special room)
    currentln[x] = "2"  # ""
    area[y] = listtostring(currentln)  # ""
    currentln = list(area[0])  # making sure the top left corner a path (the entry point to the level)
    currentln[0] = "1"  # ""
    area[0] = listtostring(currentln)  # ""
    return(area)  # returning the list of the level


def ship(size, length):
    ship = shipgen(size, length)
    x = 0
    y = 0
    area = room(x, y, ship)
    print(ship)
    print(area)


def room(x, y, ship):
    if(x < len(ship[1])and y < len(ship)/len(ship[1])):
        ypos = ship[y]
        ypos = list(ypos)
        pos = int(ypos[x])
        return(pos)


def areasdef(areasamount, syslvl):
    for i in range(0, areasamount):
        areatype = random.randint(1, 10)
        if(areatype == 1):
            var.n = var.n + 1  # n defines what number to apply to each area
            a = random.randint(1, 25) + 64  # a,b and c are ascii values of randomised letters for the names of objects
            b = random.randint(1, 25) + 64
            c = random.randint(1, 25) + 64
            areaname = "UNKNOWN-", chr(a), chr(b), chr(c), "-", str(random.randint(0, 100))  # creating the name of the object/area
            areaname = ''.join(areaname)  # joining the list of values into one string (the name)
            var.areas[var.n] = areaname
            print("\t\t| ", var.n, ". ", areaname, "\t|")
        elif(areatype == 2 or areatype == 3 or areatype == 4 or areatype == 5):  # Making it a 40% chance to see a neutral ship
            var.n = var.n + 1  # n defines what number to apply to each area
            a = random.randint(1, 25) + 64  # a,b and c are ascii values of randomised letters for the names of objects
            b = random.randint(1, 25) + 64
            c = random.randint(1, 25) + 64
            areaname = "NEUTRAL-", chr(a), chr(b), chr(c), "-", str(random.randint(0, 100))  # creating the name of the object/area
            areaname = ''.join(areaname)  # joining the list of values into one string (the name)
            var.areas[var.n] = areaname
            print("\t\t| ", var.n, ". ", areaname, "\t|")
        elif(areatype == 6 or areatype == 7):  # 20% chance of a friendly ship being generated
            var.n = var.n + 1  # n defines what number to apply to each area
            a = random.randint(1, 25) + 64  # a,b and c are ascii values of randomised letters for the names of objects
            b = random.randint(1, 25) + 64
            c = random.randint(1, 25) + 64
            areaname = "CORDIAL-", chr(a), chr(b), chr(c), "-", str(random.randint(0, 100))  # creating the name of the object/area
            areaname = ''.join(areaname)  # joining the list of values into one string (the name)
            var.areas[var.n] = areaname
            print("\t\t| ", var.n, ". ", areaname, "\t|")
        elif(areatype == 8 or areatype == 9):  # 20% chance of creating a hostile ship
            var.n = var.n+1  # n defines what number to apply to each area
            a = random.randint(1, 25) + 64  # a,b and c are ascii values of randomised letters for the names of objects
            b = random.randint(1, 25) + 64
            c = random.randint(1, 25) + 64
            areaname = "HOSTILE-", chr(a), chr(b), chr(c), "-", str(random.randint(10, 99))  # creating the name of the object/area
            areaname = ''.join(areaname)  # joining the list of values into one string (the name)
            var.areas[var.n] = areaname
            print("\t\t| ", var.n, ". ", areaname, "\t|")
        else:  # 10% chance of generating a station
            var.n = var.n+1  # n defines what number to apply to each area
            a = random.randint(1, 25) + 64  # a,b and c are ascii values of randomised letters for the names of objects
            b = random.randint(1, 25) + 64
            c = random.randint(1, 25) + 64
            areaname = "STATION-", chr(a), chr(b), chr(c), "-", str(random.randint(0, 100))  # creating the name of the object/area
            areaname = ''.join(areaname)  # joining the list of values into one string (the name)
            var.areas[var.n] = areaname
            print("\t\t| ", var.n, ". ", areaname, "\t|")
        # print(areas)
