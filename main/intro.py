import time
import random

def clear(amount):
    print("\n"*amount)


def areasdef(areasamount,syslvl): #areasdef defines the type of area in a system and its name
    global n
    n =1
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

def introscan(syslvl,scansize, logo =0): #intro should be whether or not this is the scan in the intro (1 if it is 0 if it's not)
    global n, areas, scanned
    if(logo == 1):
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
    choice = input("(scan) ")
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
        print("\nscan: do a wide scan of the local solar system")
        print("dscan: do a detailed scan of a specific location")
        print("exit: exit scan and return to shell")
        print("clear: clear the console")
    elif(choice == "dscan"): #processing input
        print("this will exit scan and take you to marauder. confirm (y/n)")
        choice = input("(scan) ")
        if(choice == "y"):
                clear(100)
                current = ""
                ships = ["","","","","","","","","","","","","","","","","","",""]
                a = 1
                if(scanned == 0):
                    print("Must scan for ships before running.")
                    scan(syslvl,scansize)
                else:
                    print("Which ship (no stations or unknown objects) do you wish to scan? (full name or value)")
                    print("type the name of the ship or 1")
                    print("\t\t _______________________")
                    while(a<=n):
                        current = str(areas[a])
                        if(current[:7] == "NEUTRAL" or current[:7] == "CORDIAL" or current[:7] == "HOSTILE"):
                            ships[a] = areas[a]
                            print("\t\t| ",a,str(ships[a]),"\t|")
                        a = a +1
                    print("\t\t|_______________________|")
        choice = input(": ")
        if(str(choice) in ships):
            print("Worked!")
            #stuff here
        elif(choice.isdigit()):
            if(int(choice) < a):
                print("Worked!")
                print(str(ships[int(choice)]))
                #stuff here

    elif(choice == "exit"):
	    console(1)
    elif(choice == "clear"):
        clear(100)
    else:
        print("scan:",choice,": command not found")
    scan(syslvl,scansize)



def introconsole(logo =0):
    global shellprompt, name, shipname
    clear(100)
    if(logo == 1):
       print("""
                 _____  _____    _____  _    _    __      _____  _  _   ___
        /\\      / ____||_   _|  / ____|| |  | |   \\ \\    / /__ \\| || | / _ \\
       /  \\    | (___    | |   | (___  | |__| |    \\ \\  / /   ) | || || (_) |
      / /\\ \\    \\___ \\   | |    \\___ \\ |  __  |     \\ \\/ /   / /|__   _\__, |
     / ____ \\ _ ____) | _| |_ _ ____) || |  | |_     \\  /   / /_ _ | |   / /
    /_/    \\_(_)_____(_)_____(_)_____(_)_|  |_(_)     \\/   |____(_)|_|  /_/
    Advanced     Ship  Interactive    Shell          Version      2.49
        """)
    print("\nThis is the console from which you will be able to use all the programs on your ship's system. \nInstall new programs or get updates for currently installed programs at space stations.")
    print("\n\nType \"help\" to view a list of commands")
    time.sleep(0.5)
    shellprompt = "[",name,"@",shipname," ~]$ "
    shellprompt = ''.join(shellprompt)
    su = 0
    choice = input(shellprompt)
    if(choice.lower() == "scan"):
        introscan(1,1,1)
    elif(choice == "help"):
        print("\nAdvanced Ship Interactive Shell Version 2.49")
        print("\nCommands available:")
        print("\nscan: scans the area around your ship.")
        print("\nmarauder: scans ships for loot, weapons and life signs.") #more commands here when implimented
        print("\nclear: clears the console")
        clear(2)
        print("Type \"scan\"")
        clear(1)
        input("Press enter to continue.")
        console(0)
    elif(choice == "clear"):
        clear(50)
        time.sleep(0.1)
        clear(50)
    else:
        print("asish:",choice,": command not found")
        console()

def intro():
    clear(100)
    print("You are a mercinary, a soldier for hire (space pirate).\nYour mission: to voyage to the centre of the galaxy and find out what lies there. \nBut for now, think a little smaller. Look for a cargo ship in this solar system by typing scan into your ship's console.")
    input("\n\nPress Enter to contine... ")
introconsole(1)
