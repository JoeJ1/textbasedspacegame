import random

def listtostring(lst): #Converts a list into a string without the special charachters of a list (brackets and commas etc.)
    lst=str(lst)
    lst=lst.replace("\"","")
    lst=lst.replace("\"","")
    lst=lst.replace("'","")
    lst=lst.replace(",","")
    lst=lst.replace("]","")
    lst=lst.replace("[","")
    lst=lst.replace(" ","")
    return(lst)

def lvlgen(size,length): #Size is the size of the square grid the level is drawn onto and length is the actual length of the path
    area = ["0"*size]*size #making the level
    choices = [""]*length #creating the list of direction choices
    x=0 #defining positional variables for the current position of the "path drawer" (drawer as in one who draws not cupboard)
    y=0 # ""
    i=0 # i is a placeholder for the current point in the list. Used to increment through a list and change each element.
    while(i<length):
        options = ["right","left","up","down"] #Creating a list of all possible directions then removing them if the path cannot go in that direction
        if(x == 0): #checking if the path drawer is at the left wall,
            options.remove("left") # if so removing the option to move left.
        if(x == len(area[y])-1): #checking if the path drawer is at the right wall,
            options.remove("right") # if so removing the option to move right.
        if(y == len(area)-1): #checking if the path drawer is at the bottom wall,
            options.remove("down") # if so removing the option to move down.
        if(y == 0): #checking to see if the path drawer is at the top wall,
            options.remove("up") # if so removing the option to move up.
        if(len(options) == 0): #checking if any direction can be moved in,
            break #if not then stop incrementing
        direction = options[random.randint(0,len(options)-1)] #randomly choosing which direction to move in from the list of possible directions
        choices[i] = direction #adding it to the list of direction choices
        i = i +1 #incrementing
    i = 0 #reseting "i" to reuse for another while loop
    while(i<len(choices)): #incrementing the list of choices
        if(choices[i] == "left"): #checking to see which direction to move in
            x = x -1 # moveing in that direction
        elif(choices[i] == "right"): # ""
            x = x +1 #""
        elif(choices[i] == "up"): #""
            y = y -1 #""
        elif(choices[i] == "down"):# ""
            y = y +1# ""
        currentln = list(area[y])#converting the list of x coordinates into x and y
        currentln[x] = "1" # making the current position 1 (a pathway)
        area[y] = listtostring(currentln) #adding that position to the list/area
        i = i +1 # incrementing "i"
    currentln = list(area[y])#making the last point in the path 2 (a special room)
    currentln[x] = "2" # ""
    area[y] = listtostring(currentln) # ""
    currentln = list(area[0]) #making sure the top left corner a path (the entry point to the level)
    currentln[0] = "1" # ""
    area[0] = listtostring(currentln) #""
    return(area) #returning the list of the level

###########################################
#unnecissarry from this point onwards. remove when implimenting (this just prints the generated area so  this program can run as a standalone, not in the main program.)
area = lvlgen(5,4)
i=0
print("\n")
while(i<len(area)):
    print(area[i])
    i=i+1
