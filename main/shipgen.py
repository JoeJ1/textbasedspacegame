import random
def shipgen(sizex,sizey):
    array = ["",]*sizey*sizex
    i = 0
    while(i<len(array)):
        array[i] = random.randint(0,2)
        i = i+1
    array[0] = 1
    string = ','.join(str(array))
    string = string.replace("[","")
    string = string.replace("]","")
    string = string.replace(",","")
    string = string.replace(" ","")
    string = [string[a:a+sizey] for a in range(0, len(string), sizey)]
    return(string)
def ship(sizex,sizey):
    ship = shipgen(sizex,sizey)
    elementlen = len(ship[1])
    x = 0
    y = 0
    area = room(x,y,ship)
    print(ship)
    print(area)
def room(x,y,ship):
    if(x<len(ship[1])and y<len(ship)/len(ship[1])):
        ypos = ship[y]
        ypos = list(ypos)
        pos = ypos[x]
        return(pos)
ship(8,4)
