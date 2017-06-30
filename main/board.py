import var
import lvlgen
import random


def shipboard():
    option1 = ""
    option2 = ""
    option3 = ""
    option4 = ""
    if(var.area[7] == "NEUTRAL"):
        level = lvlgen.shipgen(random.randint(5, 9), random.randint(6, 8))
    else:
        level = lvlgen.shipgen(random.randint(3, 7), random.randint(4, 6))
    options = optionscheck(0, 0, level)
    if(options[0] is True):
        if(option1 == ""):
            option1 = "right"
        elif(option2 == ""):
            option2 = "right"
        elif(option3 == ""):
            option3 = "right"
        else:
            option4 = "right"
    if(options[1] is True):
        if(option1 == ""):
            option1 = "left"
        elif(option2 == ""):
            option2 = "left"
        elif(option3 == ""):
            option3 = "left"
        elif(option4 == ""):
            option4 = "left"
    if(options[2] is True):
        if(option1 == ""):
            option1 = "up"
        elif(option2 == ""):
            option2 = "up"
        elif(option3 == ""):
            option3 = "up"
        elif(option4 == ""):
            option4 = "up"
    if(options[3] is True):
        if(option1 == ""):
            option1 = "down"
        elif(option2 == ""):
            option2 = "down"
        elif(option3 == ""):
            option3 = "down"
        elif(option4 == ""):
            option4 = "down"
    a = ""
    b = ""
    c = ""
    d = ""
    if(option1 != ""):
        a = "\n"
    if(option2 != ""):
        b = "\n"
    if(option3 != ""):
        c = "\n"
    if(option4 != ""):
        d = "\n"
    print("Options for movement are: ")
    print(a, option1, b, option2, c, option3, d, option4)
    print("\n")
    choice = input(": ")
    if(choice == option1 or choice == option2 or choice == option3 or choice == option4):
        if(choice.lower() == "right"):
            var.x = var.x + 1
        elif(choice.lower() == "left"):
            var.x = var.x - 1
        elif(choice.lower() == "up"):
            var.y = var.y - 1
        elif(choice.lower() == "down"):
            var.y = var.y + 1


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
