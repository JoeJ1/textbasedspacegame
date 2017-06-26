import time
import random
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

def console():
    clear(100)
    print("""
                  _____  _____    _____  _    _    __      _____  _  _   ___
         /\\      / ____||_   _|  / ____|| |  | |   \\ \\    / /__ \\| || | / _ \\
        /  \\    | (___    | |   | (___  | |__| |    \\ \\  / /   ) | || || (_) |
       / /\\ \\    \\___ \\   | |    \\___ \\ |  __  |     \\ \\/ /   / /|__   _\__, |
      / ____ \\ _ ____) | _| |_ _ ____) || |  | |_     \\  /   / /_ _ | |   / /
     /_/    \\_(_)_____(_)_____(_)_____(_)_|  |_(_)     \\/   |____(_)|_|  /_/

     Advanced     Ship  Interactive    Shell


    """)
    choice = input(": ")
    if(choice == "scan"):
        scan()


def clear(amount): #defining clear, a funcion which prints a certain amount of empty lines
    print("\n"*amount)

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

def scan(syslvl,scansize,intro = 0): #intro should be whether or not this is the scan in the intro (1 if it is 0 if it's not)
    global n, areas, scanned
    clear(100) #100 lines of nothing
    print("""
           _____                        ____  _  _  __
          / ____|                      |___ \\| || |/_ |
         | (___   ___ __ _ _ __   __   ____) | || |_| |
          \\___ \\ / __/ _` | '_ \\  \\ \\ / /__ <|__   _| |
          ____) | (_| (_| | | | |  \\ V /___) |  | | | |
         |_____/ \\___\\__,_|_| |_|   \\_/|____(_) |_| |_|
    """)
    time.sleep(0.5)
    areasamount = random.randint(1,(scansize*syslvl))
    print("\t\t _______________________") #the box around the objects displayed in the scanner
    if(scanned == 0):
        areasdef(areasamount,syslvl,intro)
        scanned = 1
    else:
        i = 1
        while(i<=n):
            print("\t\t| ",i,". ",str(areas[i]),"\t|")
            i= i+1

    print("\t\t|_______________________|") # the bottom half of the box around objects in the scanner
    #print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
    print("\nType \"h\" to show help.")
    choice = input(": ") # taking input from player
    if(choice == "h" or choice == "help" or choice == "H" or choice == "Help" or choice == "HELP"):
        print("\n\nDo you wish to:\n\t1. scan a chosen object in more detail, for life signs, weaponry etc.\n\t2. Fly to the chosen object and prepare to dock/board/land.\n\t3. Exit Scanner")
        choice = input(":")
        if(choice == "scan" or choice == "1" or choice == "one" or choice == "One" or choice == "Scan" or choice == "SCAN" or choice == "s" or choice == "S" or choice == "1k."): #processing input
            print("Which object would you like to scan in detail? (full name or value)")
            choice = input(": ")
            if(choice.isdigit() and int(choice)<n):
                print("choice correct") #for debugging purposes
                #stuff here
            elif(str(choice) in areas):
                print("choice correct") #for debugging purposes
            else:
                print("that wasn\'t one of the options")
                scan(syslvl,scansize,intro)
                #stuff here
        elif(choice == "2" or choice == "two" or choice == "Two" or choice == "Fly" or choice == "fly" or choice == "dock" or choice == "board"):
            print("Which object would you like to fly to? (full name or value)")
            choice = input(": ")
            #stuff here
    if(choice == "scan" or choice == "1" or choice == "one" or choice == "One" or choice == "Scan" or choice == "SCAN" or choice == "s" or choice == "S" or choice == "1k."): #processing input
        print("Which object would you like to scan in detail? (full name or value)")
        choice = input(": ")
        if(choice.isdigit() and int(choice)<n):
            print("choice correct") #for debugging purposes
            #stuff here
        elif(str(choice) in areas):
            print("choice correct") #for debugging purposes
        else:
            print("that wasn\'t one of the options")
            scan(syslvl,scansize,intro)
            #stuff here
    elif(choice == "2" or choice == "two" or choice == "Two" or choice == "Fly" or choice == "fly" or choice == "dock" or choice == "board"):
        print("Which object would you like to fly to? (full name or value)")
        choice = input(": ")
        #stuff here

def intro():
    clear(100)
    print("You are a ruthless mercenary, a soldier for hire (space pirate).\nYour mission: to reach the centre of the galaxy and discover what lies there.\nBut for now, think a little smaller, outside your window in the distance you see a small ship, some quick scans tell you there might be weapons aboard.\nBoard it kill any hostiles and leave with the weapons") #flavour text
    input("Press enter to continue... ") #so the player can choose when to move on
    clear(100) # clearing the screen
    print("Type \"scan\" or \"s\" to scan for nearby objects in space") #telling the player how to use the scanner
    choice = input(": ") #taking player's input
    if(choice == "scan" or choice == "s" or choice == "Scan" or choice == "S" or choice == "SCAN"): #processing input
        scan(1,10)#(a,b,c) a=system level, b = scan size, c = whether or not the player is in the tutorial mission (1/0,t/f)
        scanned = 1
    else:
        print("please type \"scan\" or \"s\"") #if the player doesn't type scan or s then prompt again
        time.sleep(1)
        intro()

print("Best viewed in fullscreen.")
time.sleep(1)
clear(100)
if(input("Do you wish to skip intro/tuorial? (y/n)") == "n"): #deciding whether or not to call intro
    intro()#calling intro mission
