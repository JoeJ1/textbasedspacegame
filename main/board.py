import var
import levelgen
def shipboard():
    option1 = ""
    option2 = ""
    option3 = ""
    option4 = ""
    if(var.area[7] == "NEUTRAL"):
        level = shipgen(randint(5,9),randint(6,8))
    else:
        level = shipgen(randint(3,7),randint(4,6))
    options = optionscheck(0,0,level)
    if(options[0] == True):
        if(option1 == ""):
            option1 = "right"
        elif(option2 == ""):
            option2 = "right"
        elif(option3 == ""):
            option3 = "right"
        else:
            option4 = "right"
    if(options[1] = True):
        if(option1 == ""):
            option1 = "left"
        elif(option2 == ""):
            option2 = "left"
        elif(option3 == ""):
            option3 = "left"
        elif(option4 == ""):
            option4 = "left"
    if(options[2] = True):
        if(option1 == ""):
            option1 = "up"
        elif(option2 == ""):
            option2 = "up"
        elif(option3 == ""):
            option3 = "up"
        elif(option4 == ""):
            option4 = "up"
    if(options[3] = True):
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
    print(a,option1,b,option2,c,option3,d,option4)

def optionscheck(x,y,level):
    rightoption = False
    leftoption = False
    upoption = False
    downoption = False
    if(levelgen.room(x+1,y,level) == 1 or levelgen.room(x+1,y,level) == 2):
        rightoption = True
    if(levelgen.room(x-1,y,level) == 1 or levelgen.room(x-1,y,level) == 2):
        leftoption = True
    if(levelgen.room(x,y+1,level) == 1 or levelgen.room(x,y+1,level) == 2):
        downoption = True
    if(levelgen.room(x,y-1,level) == 1 or levelgen.room(x,y-1,level) == 2):
        upoption = True
    options = [rightoption,leftoption,upoption,downoption]
    return(options)
