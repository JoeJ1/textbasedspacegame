import random
import time
import console
scanned = 0
areas = ["","","","","","","","","","","","","",""] #defining the array of areas
def clear(amount): #defining clear, a funcion which prints a certain amount of empty lines
    print("\n"*amount)

def scan(syslvl,scansize,logo): #intro should be whether or not this is the scan in the intro (1 if it is 0 if it's not)
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
        print("this will perform a detailed scan of an object. confirm (y/n)")
        choice = input("(scan) ")
        if(choice == "y"):
            dscan(1,1)
    elif(choice == "exit"):
	    console.console(1)
    elif(choice == "clear"):
        clear(100)
    else:
        print("scan:",choice,": command not found")
    scan(syslvl,scansize,0)

def areasdef(areasamount,syslvl,intro = 0): #areasdef defines the type of area in a system and its name
    global n
    if(intro == 1): #checking whether or not the player is in the intro/tutorial (if so it always creates a neutral ship
        n =0
        a = random.randint(1,25) + 64 #a,b and c are ascii values of randomised letters for the names of objects
        b = random.randint(1,25) + 64
        c = random.randint(1,25) + 64
        areaname = "NEUTRAL-",chr(a),chr(b),chr(c),"-",str(random.randint(0,100)) #creating the name of the object/area
        areaname = ''.join(areaname) #joining the list of values into one string (the name)
        print("\t\t| \/value  \/full name\t|")
        print("\t\t|",areaname,"\t|")
        areas[n] = areaname
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
                areas[n] = areaname
                print("\t\t| ",n,". ",areaname,"\t|")
            elif(areatype ==2 or areatype ==  3 or areatype == 4 or areatype == 5): #Making it a 40% chance to see a neutral ship
                n = n+1 # n defines what number to apply to each area
                a = random.randint(1,25) + 64 #a,b and c are ascii values of randomised letters for the names of objects
                b = random.randint(1,25) + 64
                c = random.randint(1,25) + 64
                areaname = "NEUTRAL-",chr(a),chr(b),chr(c),"-",str(random.randint(0,100))  #creating the name of the object/area
                areaname = ''.join(areaname) #joining the list of values into one string (the name)
                areas[n] = areaname
                print("\t\t| ",n,". ",areaname,"\t|")
            elif(areatype == 6 or areatype == 7): #20% chance of a friendly ship being generated
                n = n+1 # n defines what number to apply to each area
                a = random.randint(1,25) + 64 #a,b and c are ascii values of randomised letters for the names of objects
                b = random.randint(1,25) + 64
                c = random.randint(1,25) + 64
                areaname = "CORDIAL-",chr(a),chr(b),chr(c),"-",str(random.randint(0,100)) #creating the name of the object/area
                areaname = ''.join(areaname) #joining the list of values into one string (the name)
                areas[n] = areaname
                print("\t\t| ",n,". ",areaname,"\t|")
            elif(areatype == 8 or areatype == 9): #20% chance of creating a hostile ship
                n = n+1 # n defines what number to apply to each area
                a = random.randint(1,25) + 64 #a,b and c are ascii values of randomised letters for the names of objects
                b = random.randint(1,25) + 64
                c = random.randint(1,25) + 64
                areaname = "HOSTILE-",chr(a),chr(b),chr(c),"-",str(random.randint(10,99)) #creating the name of the object/area
                areaname = ''.join(areaname) #joining the list of values into one string (the name)
                areas[n] = areaname
                print("\t\t| ",n,". ",areaname,"\t|")
            else: # 10% chance of generating a station
                n = n+1 # n defines what number to apply to each area
                a = random.randint(1,25) + 64 #a,b and c are ascii values of randomised letters for the names of objects
                b = random.randint(1,25) + 64
                c = random.randint(1,25) + 64
                areaname = "STATION-",chr(a),chr(b),chr(c),"-",str(random.randint(0,100)) #creating the name of the object/area
                areaname = ''.join(areaname) #joining the list of values into one string (the name)
                areas[n]=areaname
                print("\t\t| ",n,". ",areaname,"\t|")
        #print(areas)

def dscan(syslvl,scanned):
    global areas,n
    clear(100)
    current = ""
    ships = ["","","","","","","","","","","","","","","","","","",""]
    a = 1
    if(scanned == 0):
        print("Must scan for ships before running.")
    else:
        print("Which ship (no stations or unknown objects) do you wish to scan? (full name or value)")
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
