import var
import lvlgen
def mapgen(ship):
    mapstr = ship
    x = 0
    y = 0
    i = 0
    while(i<len(mapstr)):
        if(mapstr[i] != "0"):
            if(lvlgen.room(x+1,y,ship) == "0" and lvlgen.room(x-1,y,ship) == "0" and lvlgen.room(x,y+1) == "0" and lvlgen.room(x,y-1) == "0"):
                lvlgen[i] == "0"
        i = i +1
    i = 0
    while(i<len(mapstr)):
        mapstr[i] = str(mapstr[i]).replace("0","░")
        mapstr[i] = str(mapstr[i]).replace("1","█")
        mapstr[i] = str(mapstr[i]).replace("2","█")
        mapstr[i] = str(mapstr[i]).replace("3","█")
        mapstr[i] = str(mapstr[i]).replace("4","█")
        mapstr[i] = str(mapstr[i]).replace("5","█")
        mapstr[i] = str(mapstr[i]).replace("6","█")
        mapstr[i] = str(mapstr[i]).replace("7","█")
        mapstr[i] = str(mapstr[i]).replace("8","█")
        mapstr[i] = str(mapstr[i]).replace("9","█")

        print(mapstr[i])
        i = i +1


mapgen(lvlgen.shipgen(100,100))
