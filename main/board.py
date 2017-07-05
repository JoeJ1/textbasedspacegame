import var
import lvlgen
import random
import map

def shipboard(newgen = True):
    if(newgen == True):
        if(var.area[7] == "NEUTRAL"):
            level = lvlgen.shipgen(random.randint(5, 9), random.randint(6, 8))
            var.areamap = lvlgen.shipgen(random.randint(5, 9), random.randint(6, 8))
        else:
            level = lvlgen.shipgen(random.randint(3, 7), random.randint(4, 6))
            var.areamap = lvlgen.shipgen(random.randint(3, 7), random.randint(4, 6))
        options = optionscheck(0, 0, level)
    else:
        level = var.areamap




def optionscheck(x, y, level):
    rightoption = False
    leftoption = False
    upoption = False
    downoption = False
    if(lvlgen.room(x+1, y, level) == 1 or lvlgen.room(x+1, y, level) == 2):
        rightoption = True
    if(lvlgen.room(x-1, y, level) == 1 or lvlgen.room(x-1, y, level) == 2):
        leftoption = True
    if(lvlgen.room(x, y+1, level) == 1 or lvlgen.room(x, y+1, level) == 2):
        downoption = True
    if(lvlgen.room(x, y-1, level) == 1 or lvlgen.room(x, y-1, level) == 2):
        upoption = True
    options = [rightoption, leftoption, upoption, downoption]
    return(options)


def parser(room,x,y):
    options = [""]
    i = 0
    diroptions = optionscheck(x,y,var.areamap)
    while(i<[diroptions])
        if(diroptions[0] is True):
            options[i] = dirflvtxtE[random.randint(0,len(dirflvtxtE))]
        if(diroptions[1] is True):
            options[i] = dirflvtxtW[random.randint(0,len(dirflvtxtW))]
        if(diroptions[2] is True):
            options[i] = dirflvtxtN[random.randint(0,len(dirflvtxtN))]
        if(diroptions[3] is True):
            options[i] = dirflvtxtS[random.randint(0,len(dirflvtxtS))]
        i = i +1
    dirflvtxtE = ["There is a small steel door leading east.","There is a large, hydraulic door to the east.", "To the east you see a small mechanical door.", "On your east you see an open door, You can't see what's in the next room, however, as it curves around a corner."]
    dirflvtxtW = ["There is a small steel door leading west.","There is a large, hydraulic door to the west.", "To the west you see a small mechanical door.", "On your west you see an open door, You can't see what's in the next room, however, as it curves around a corner."]
    dirflvtxtN = ["There is a small dented steel door leading north.","There is a large, hydraulic door to the north.", "To the north you see a small mechanical door.", "On your north you see an open door, You can't see what's in the next room, however, as it curves around a corner."]
    dirflvtxtS = ["There is a small steel door leading south.","There is a large, hydraulic door to the south.", "To the south you see a large rusting door.", "On your south you see an open door, You can't see what's in the next room, however, as it curves around a corner."]

    objects = objectsgen(room)
    if("glass" in objects):
        i = i + 1
        options[i] = random.choice(["Shattered glass lies strewn across the cold metal floor.", "Small fragments of glass litter the floor.", "Glass, shattered, perhaps in some past struggle, lies all around the room", "Smashed glass lies on the ground, it looks sharp enough to do some serious damage."]) #insert glass flavour text here
    if("gun" in objects):
        i = i +1
        if("table" in objects):
            options[i] = random.choice(["A small pistol lies on the table, left carelessly by a member of the crew.","A gun is on the table."])
        else:
            options[i] = random.choice(["A gun is on the floor.","A gun lies thrown carlessly on the hard floor."])
    if("table" in objects):
        i = i +1
        options[i] = random.choice([])


def objectsgen(room):
    objectoptions = ["glass","gun","table","chair","unit 1","unit 2","unit 5","unit 25","unit 100","wires"] #put objects here to add them to the rooms
    chosenobjects = [""]
    objectsamount = random.randing(0,6)
    i = 0
    while(i<objectsamount):
        random = random.randint(1,len(objectoptions))
        chosenobjects[i] = objectoptions[random]
        i = i +1
    return(chosenobjects)
