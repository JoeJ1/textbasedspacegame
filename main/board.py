import var
import lvlgen
import random
import map  # TODO rename map please


def shipboard(newgen=True):
    var.areatype = var.area[7]


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


def parser(room, x, y):
    global objects
    options = [""]
    i = 0
    diroptions = optionscheck(x, y, var.areamap)
    while(i < [diroptions]):
        if(diroptions[0] is True):
            options[i] = random.choice(["There is a small steel door leading east.", "There is a large, hydraulic door to the east.", "To the east you see a small mechanical door.", "On your east you see an open door, You can't see what's in the next room, however, as it curves around a corner."])
        if(diroptions[1] is True):
            options[i] = random.choice(["There is a small steel door leading west.", "There is a large, hydraulic door to the west.", "To the west you see a small mechanical door.", "On your west you see an open door, You can't see what's in the next room, however, as it curves around a corner."])
        if(diroptions[2] is True):
            options[i] = random.choice(["There is a small dented steel door leading north.", "There is a large, hydraulic door to the north.", "To the north you see a small mechanical door.", "On your north you see an open door, You can't see what's in the next room, however, as it curves around a corner."])
        if(diroptions[3] is True):
            options[i] = random.choice(["There is a small steel door leading south.", "There is a large, hydraulic door to the south.", "To the south you see a large rusting door.", "On your south you see an open door, You can't see what's in the next room, however, as it curves around a corner."])
        i = i + 1

    var.objects = objectsgen(room)
    if("glass" in objects):
        i = i + 1
        options[i] = random.choice(["Shattered glass lies strewn across the cold metal floor.", "Small fragments of glass litter the floor.", "Glass, shattered, perhaps in some past struggle, lies all around the room", "Smashed glass lies on the ground, it looks sharp enough to do some serious damage."])  # insert glass flavour text here
    if("table" in objects):
        i = i + 1
        if("chair" in objects):
            options[i] = random.choice(["A small chair is positioned behind a large elaborately patterned table in the corner of the room.", "A small chair sits behind a blood stained table at an angle in the centre of the room."])
        else:
            options[i] = random.choice(["A large, elaborately patterned table sits in the corner.", "A small, stained table sits at an angle in the centre of the room"])

    if("gun" in objects):
        i = i + 1
        if("table" in objects):
            options[i] = random.choice(["A small pistol lies on the table, left carelessly by a member of the crew.", "A gun is on the table."])
        else:
            options[i] = random.choice(["A gun is on the floor.", "A gun lies thrown carlessly on the hard floor."])
    if("unit 1" in objects or "unit 2" in objects or "unit 5" in objects or "unit 25" in objects or "unit 100" in objects):
        i = i + 1
        options[i] = random.choice(["A small jar of units lies in the middle of the table.", ""])
    if("wires" in objects):
        i = i + 1
        options[i] = random.choice(["Wires lay strewn randomly across the floor", "Wires stick out of the wall, they don't look as though they've carried an current in years."])


def objectsgen(room):
    objectoptions = ["glass", "gun", "table", "chair", "unit 1", "unit 2", "unit 5", "unit 25", "unit 100", "wires"]  # put objects here to add them to the rooms
    chosenobjects = [""]
    objectsamount = random.randint(0, 6)
    i = 0
    while(i < objectsamount):
        chosenobjects[i] = objectoptions[random.randint(1, len(objectoptions))]
        i = i + 1
    return(chosenobjects)
