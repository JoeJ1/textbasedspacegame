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
    choices = [""]*length
    x=0
    y=0

    i=0
    while(i<length):
        options = ["right","left","up","down"]
        if(x == 0):
            options.remove("left")
        if(x == len(area[y])-1):
            options.remove("right")
        if(y == len(area)-1):
            options.remove("down")
        if(y == 0):
            options.remove("up")
        print(options)
        if(len(options) == 0):
            break
        direction = options[random.randint(0,len(options)-1)]
        choices[i] = direction
        print(choices[i],x,y)
        i = i +1
    i = 0
    print(choices)
    while(i<len(choices)):
        if(choices[i] == "left"):
            x = x -1
        elif(choices[i] == "right"):
            x = x +1
        elif(choices[i] == "up"):
            y = y -1
        elif(choices[i] == "down"):
            y = y +1
        currentln = list(area[y])
        currentln[x] = "1"
        area[y] = listtostring(currentln)
        i = i +1
    currentln = list(area[y])
    currentln[x] = "2"
    area[y] = listtostring(currentln)
    currentln = list(area[0])
    currentln[0] = "1"
    area[0] = listtostring(currentln)
    return(area)
area = lvlgen(5,4)
i=0
print("\n")
while(i<len(area)):
    print(area[i])
    i=i+1
