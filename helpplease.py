#This is me attempting to make a better way of randomly generating the levels but it doesn't work.
import random
size = 5
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
def diroptionsgen(area,x,y):
    currentln = area[y]
    options = ["right","left","up","down"]
    if(x == len(currentln)):
        options[0] = ""
    if(x == 0):
        options[1] = ""
    if(y == len(listtostring(area))):
        options[3] = ""
    if(y == 0):
        options[2] = ""
    return(options)

def lvlgen(size,length):
    area = ["0"*size]*size
    x=0
    y=0
    i=0
    while(i<length):
        diroptions = diroptionsgen(area,x,y)
        direction = random.choice(diroptions)
        currentln = list(area[y])
        currentln[x] = "1"
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
            direction=random.choice(diroptions)
        else:
            currentln=listtostring(currentln)
            area[y] = currentln
    currentln = list(area[0])
    currentln[0] = "1"
    area[0] = listtostring(currentln)
    return(area)
area = lvlgen(10,9)
i=0
while(i<len(area)):
    print(area[i])
    i=i+1
