def roomtest():
    print("\n"*2)
    objects = ["gun", "wires", "door", "glass"]
    print("You enter a cold, dark room.")
    objectstr = str(objects)
    if(len(objects) > 0):
        if("door" in objects):
            print("You see a large metal door.")
        if("gun" in objects):
            print("On the floor a small pistol lies forgotten.")
        if("wires" in objects):
            print("Wires litter the ground.")
        if("glass" in objects):
            print("Shattered glass lies strewn across the patched metal floor.")
    choice = input(": ")
    choicelist = choice.split()
    choiceverb = choicelist[0]
    if(len(choicelist) > 1):
        choiceparameter = choicelist[1]
    else:
        choiceparameter = ""
    inventory = [""]
    inventoryplace = 0
    print(choiceverb)
    print(choiceparameter)
    if(choiceverb == "pickup"):
        if(choiceparameter == ""):
            print("pick up what?")
        if(choiceparameter.lower() == "gun" or choiceparameter.lower() == "pistol"):
            i = 0
            while(i < len(objects)):
                if(objects[i] == "gun"):
                    objects[i] = ""
                    inventory[inventoryplace] = "gun"
                    inventoryplace = inventoryplace + 1
                    print("picked up", choiceparameter)
                else:
                    i = i + 1
            if(i > len(objects)):
                print("You can't pick that up")
        if(choiceparameter.lower() == "wires" or choiceparameter.lower() == "cables"):
            i = 0
            while(i < len(objects)):
                if(objects[i] == "wires"):
                    objects[i] = ""
                    inventory[inventoryplace] = "wires"
                    inventoryplace = inventoryplace + 1
                    print("picked up ", choiceparameter)
                else:
                    i = i + 1
            if(i > len(objects)):
                print("You can't pick that up")
        if(choiceparameter.lower() == "door" or choiceparameter.lower() == "metaldoor"):
            print("You can't pick that up")
        if(choiceparameter.lower() == "glass" or choice.lower() == "shatteredglass"):
            i = 0
            while(i < len(objects)):
                    if(objects[i] == "glass"):
                        objects[i] = ""
                        inventory[inventoryplace] = "glass"
                        inventoryplace = inventoryplace + 1
                        print("picked up ", choiceparameter)
                    else:
                        i = i + 1
            if(i > len(objects)):
                print("You can't pick that up")
    elif(choiceverb.lower() == "inventory" or choiceverb.lower() == "carrying"):
        i = 0
        print("you have: ")
        while(i <= len(inventory)):
            print(inventory[i])
            i = i+1
        if(len(inventory) == 1):
            print("Nothing. Bad luck dood")
    roomtest()


roomtest()
