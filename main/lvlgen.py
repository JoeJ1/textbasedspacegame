import random
import var


def shipgen(sizex, sizey):
    array = ["", ]*sizey*sizex
    i = 0
    while(i < len(array)):
        array[i] = random.randint(0, 2)
        i = i+1
    array[0] = 1
    string = ','.join(str(array))
    string = string.replace("[", "")
    string = string.replace("]", "")
    string = string.replace(",", "")
    string = string.replace(" ", "")
    string = [string[a:a+sizey] for a in range(0, len(string), sizey)]
    return(string)


def ship(sizex, sizey):
    ship = shipgen(sizex, sizey)
    x = 0
    y = 0
    area = room(x, y, ship)
    print(ship)
    print(area)


def room(x, y, ship):
    if(x < len(ship[1])and y < len(ship)/len(ship[1])):
        ypos = ship[y]
        ypos = list(ypos)
        pos = ypos[x]
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
