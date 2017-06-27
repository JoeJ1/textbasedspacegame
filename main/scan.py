import random
import time
import marauder

a1 = "" #A variables are the names of the ship that the player sees
a2 = ""
a3 = ""
a4 = ""
a5 = ""
a6 = ""
a7 = ""
a8 = ""
a9 = ""
a10 = ""
b1 = 0 #b variables are used to define the type of ship, only used for calculations, never seen by player
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0
b8 = 0
b9 = 0
b10 = 0
areas = ["","","","","","","","","","","","","",""] #defining the array of areas
scanned = 0

def clear(amount): #defining clear, a funcion which prints a certain amount of empty lines
    print("\n"*amount)

def scan(syslvl,scansize): #intro should be whether or not this is the scan in the intro (1 if it is 0 if it's not)
    global n, areas, scanned
    print("""
          _____                        ____  _  _  __
          / ____|                      |___ \\| || |/_ |
         | (___   ___ __ _ _ __   __   ____) | || |_| |
          \\___ \\ / __/ _` | '_ \\  \\ \\ / /__ <|__   _| |
          ____) | (_| (_| | | | |  \\ V /___) |  | | | |
         |_____/ \\___\\__,_|_| |_|   \\_/|____(_) |_| |_|
    """)
    print("Welcome to Scan v3.41! Type \"help\" to view a list of commands.")
    time.sleep(0.5)
    areasamount = random.randint(1,(scansize*syslvl))
    choice = input("scan: ")
    if(choice == "scan"):
        print("\t\t _______________________") #the box around the objects displayed in the scanner
        if(scanned == 0):
            areasdef(areasamount,syslvl)
            scanned = 1
        else:
            i = 1
            while(i<=n):
                print("\t\t| ",i,". ",str(areas[i]),"\t|")
                i= i+1
                print("\t\t|_______________________|") # the bottom half of the box around objects in the scanner
    elif(choice.lower() == "help"):
        print("scan: do a wide scan of the local solar system")
        print("dscan: do a detailed scan of a specific location")
        print("exit: exit scan and return to shell")
        print("clear: clear the console")
    elif(choice == "dscan"): #processing input
        print("this will exit scan and take you to marauder. confirm (y/n)")
        choice = input("scan: ")
        if(choice == "y"):
            marauder.marauder(syslvl,scanned)
    elif(choice == "exit"):
	    console(1)
    elif(choice == "clear"):
        clear(100)
    else:
        print("scan:",choice,": command not found")
    scan(syslvl,scansize)

def areasdef(areasamount,syslvl,intro = 0): #areasdef defines the type of area in a system and its name
    global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,n
    if(intro == 1): #checking whether or not the player is in the intro/tutorial (if so it always creates a neutral ship
        n =0
        a = random.randint(1,25) + 64 #a,b and c are ascii values of randomised letters for the names of objects
        b = random.randint(1,25) + 64
        c = random.randint(1,25) + 64
        areaname = "NEUTRAL-",chr(a),chr(b),chr(c),"-",str(random.randint(0,100)) #creating the name of the object/area
        areaname = ''.join(areaname) #joining the list of values into one string (the name)
        print("\t\t| \/value  \/full name\t|")
        print("\t\t|",areaname,"\t|")
        a1 = areaname
        areas[n] = a1
        b1 = "NEU"
    elif(intro == 0):
        n =0
        for i in range(0,areasamount):
            areatype = random.randint(1,10) #10% chance to see an unknown object (asteroid, debris, distress signal, whatever)
            if(areatype == 1):
                n = n +1 # n defines what number to apply to each area
                a = random.randint(1,25) + 64 #a,b and c are ascii values of randomised letters for the names of objects
                b = random.randint(1,25) + 64
                c = random.randint(1,25) + 64
                areaname = "UNKNOWN-",chr(a),chr(b),chr(c),"-",str(random.randint(0,100)) #creating the name of the object/area
                areaname = ''.join(areaname) #joining the list of values into one string (the name)
                a1 = areaname
                b1 = "UNK"
                areas[n] = a1
                print("\t\t| ",n,". ",a1,"\t|")
            elif(areatype ==2 or areatype ==  3 or areatype == 4 or areatype == 5): #Making it a 40% chance to see a neutral ship
                n = n+1 # n defines what number to apply to each area
                a = random.randint(1,25) + 64 #a,b and c are ascii values of randomised letters for the names of objects
                b = random.randint(1,25) + 64
                c = random.randint(1,25) + 64
                areaname = "NEUTRAL-",chr(a),chr(b),chr(c),"-",str(random.randint(0,100))  #creating the name of the object/area
                areaname = ''.join(areaname) #joining the list of values into one string (the name)
                if(a2 == ""): #checking to see whether or not to override the variables
                    b2 = "NEU"
                    a2 = areaname
                    areas[n] = a2
                elif(a3 == ""):
                    a3 = areaname
                    b3 = "NEU"
                    areas[n] = a3
                elif(a4 == ""):
                    a4 = areaname
                    b4 = "NEU"
                    areas[n] = a4
                elif(a5 == ""):
                    a5 = areaname
                    b5 = "NEU"
                    areas[n] = a5
                print("\t\t| ",n,". ",areaname,"\t|")
            elif(areatype == 6 or areatype == 7): #20% chance of a friendly ship being generated
                n = n+1 # n defines what number to apply to each area
                a = random.randint(1,25) + 64 #a,b and c are ascii values of randomised letters for the names of objects
                b = random.randint(1,25) + 64
                c = random.randint(1,25) + 64
                areaname = "CORDIAL-",chr(a),chr(b),chr(c),"-",str(random.randint(0,100)) #creating the name of the object/area
                areaname = ''.join(areaname) #joining the list of values into one string (the name)
                if(a6 == ""): #checking to see whether or not to override the variables
                    b6 = "FRE"
                    a6 = areaname
                    areas[n] = a6
                elif(a7 == ""):
                    b7 = "FRE"
                    a7 = areaname
                    areas[n] = a7
                print("\t\t| ",n,". ",areaname,"\t|")
            elif(areatype == 8 or areatype == 9): #20% chance of creating a hostile ship
                n = n+1 # n defines what number to apply to each area
                a = random.randint(1,25) + 64 #a,b and c are ascii values of randomised letters for the names of objects
                b = random.randint(1,25) + 64
                c = random.randint(1,25) + 64
                areaname = "HOSTILE-",chr(a),chr(b),chr(c),"-",str(random.randint(10,99)) #creating the name of the object/area
                areaname = ''.join(areaname) #joining the list of values into one string (the name)
                if(a8 == ""): #checking to see whether or not to override the variables
                    b8 = "HOS"
                    a8 = areaname
                    areas[n] = a8
                elif(a9 == ""):
                    b9 = "HOS"
                    a9 = areaname
                    areas[n] = a9
                print("\t\t| ",n,". ",areaname,"\t|")
            else: # 10% chance of generating a station
                n = n+1 # n defines what number to apply to each area
                a = random.randint(1,25) + 64 #a,b and c are ascii values of randomised letters for the names of objects
                b = random.randint(1,25) + 64
                c = random.randint(1,25) + 64
                areaname = "STATION-",chr(a),chr(b),chr(c),"-",str(random.randint(0,100)) #creating the name of the object/area
                areaname = ''.join(areaname) #joining the list of values into one string (the name)
                b10 = "STA"
                a10 = areaname
                areas[n]=a10
                print("\t\t| ",n,". ",areaname,"\t|")
        #print(areas)
