#link: https://repl.it/J4D4/0
#sorry for the incredibly poorly written code, I
#wrote this in the notes app on my phone and
#I didn't have wifi to look up syntax so it might
#not even make sense.

import random

def listtostring(lst):
    lst=str(lst)
    lst=lst.replace("\"","")
    lst=lst.replace("\"","")
    lst=lst.replace("'","")
    lst=lst.replace(",","")
    lst=lst.replace("]","")
    lst=lst.replace("[","")
    lst=lst.replace(" ","")
    return(lst)
def lvlgen(size,length):
    global x, y, area
    area = ["0"*size]*size
    x=1
    y=0
    i=0
    while(i<length):
        currentln = list(area[y])
        options = ["right","left","up","down"]
        if(x == len(currentln)):
            options.remove("right")
        else:
            if(currentln[x+1] == "1"):
                options.remove("right")
        if(x == 0):
            options.remove("left")
        else:
            if(currentln[x-1] == "1"):
                options.remove("left")
        if(y == len(listtostring(area))):
            options.remove("down")
        else:
            if(currentln[y+1] == "1"):
                options.remove("down")
        if(y == 0):
            options.remove("up")
        else:
            if(currentln[y-1] == "1"):
                options.remove("up")
        if(len(options) == 0):
            options.append(" ")
        direction = options[random.randint(0,len(options)-1)]
        print(direction)
        if(direction=="right"):
            x=x+1
            i=i+1
        elif(direction=="left"):
            x=x-1
            i=i+1
        elif(direction=="up"):
            y=y-1
            i=i+1
        elif(direction=="down"):
            y=y+1
            i=i+1
        elif(direction==""or direction==" "):
            break
        area[y] = listtostring(currentln)
        i = i +1
    currentln[x] = "1"
    currentln = list(area[0])
    currentln[0] = "1"
    area[0] = listtostring(currentln)
    i = len(area[i])-1
    while(area[i] == "0"*size):
        del area[i]
        i = i -1
    return(area)
area = lvlgen(5,4)
i=0
while(i<len(area)):
    print(area[i])
    i=i+1
