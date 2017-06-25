import time
import random
a1 = ""
a2 = ""
a3 = ""
a4 = ""
a5 = ""
a6 = ""
a7 = ""
a8 = ""
a9 = ""
a10 = ""
b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0
b8 = 0
b9 = 0
b10 = 0
def clear(amount):
    print("\n"*amount)


def areasdef(areasamount,syslvl,intro = 0):
    global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10
    if(intro == 1):
        a = random.randint(1,25) + 64
        b = random.randint(1,25) + 64
        c = random.randint(1,25) + 64
        areaname = "1. NEUTRAL-",chr(a),chr(b),chr(c),"-",str(random.randint(0,100))
        areaname = ''.join(areaname)
        if(a2 == ""):
            b2 = "NEU"
            a2 = areaname
        elif(a3 == ""):
            a3 = areaname
            b3 = "NEU"
        elif(a4 == ""):
            a4 = areaname
            b4 = "NEU"
        elif(a5 == ""):
            a5 = areaname
            b5 = "NEU"
        print("\t\t|",areaname,"\t|")
    elif(intro == 0):
        n =0
        for i in range(0,areasamount):
            areatype = random.randint(1,10)
            if(areatype == 1):
                n = n +1
                a = random.randint(1,25) + 64
                b = random.randint(1,25) + 64
                c = random.randint(1,25) + 64
                areaname = str(n),". UNKNOWN-",chr(a),chr(b),chr(c),"-",str(random.randint(0,100))
                areaname = ''.join(areaname)
                a1 = areaname
                b1 = "UNK"
                print("\t\t|",areaname,"\t|")
            elif(areatype ==2 or areatype ==  3 or areatype == 4 or areatype == 5):
                n = n+1
                a = random.randint(1,25) + 64
                b = random.randint(1,25) + 64
                c = random.randint(1,25) + 64
                areaname = str(n),". NEUTRAL-",chr(a),chr(b),chr(c),"-",str(random.randint(0,100))
                areaname = ''.join(areaname)
                if(a2 == ""):
                    b2 = "NEU"
                    a2 = areaname
                elif(a3 == ""):
                    a3 = areaname
                    b3 = "NEU"
                elif(a4 == ""):
                    a4 = areaname
                    b4 = "NEU"
                elif(a5 == ""):
                    a5 = areaname
                    b5 = "NEU"
                print("\t\t|",areaname,"\t|")
            elif(areatype == 6 or areatype == 7):
                n = n+1
                a = random.randint(1,25) + 64
                b = random.randint(1,25) + 64
                c = random.randint(1,25) + 64
                areaname = str(n),". FRIENDLY-",chr(a),chr(b),chr(c),"-",str(random.randint(0,100))
                areaname = ''.join(areaname)
                if(a6 == ""):
                    b6 = "FRE"
                    a6 = areaname
                if(a7 == ""):
                    b7 = "FRE"
                    b6 = areaname
                print("\t\t|",areaname,"\t|")
            elif(areatype == 8 or areatype == 9):
                n = n+1
                a = random.randint(1,25) + 64
                b = random.randint(1,25) + 64
                c = random.randint(1,25) + 64
                areaname = str(n),". HOSTILE-",chr(a),chr(b),chr(c),"-",str(random.randint(0,100))
                areaname = ''.join(areaname)
                if(a8 == ""):
                    b8 = "HOS"
                    a8 = areaname
                elif(a9 == ""):
                    b9 = "HOS"
                    a9 = areaname
                print("\t\t|",areaname,"\t|")
            else:
                n = n+1
                a = random.randint(1,25) + 64
                b = random.randint(1,25) + 64
                c = random.randint(1,25) + 64
                areaname = str(n),". STATION-",chr(a),chr(b),chr(c),"-",str(random.randint(0,100))
                areaname = ''.join(areaname)
                b10 = "STA"
                a10 = areaname
                print("\t\t|",areaname,"\t|")

def scan(syslvl,scansize,intro = 0): #intro should be whether or not this is the scan in the intro (1 if it is 0 if it's not)
    clear(100)
    print("""
             __
            / _\\ ___ __ _ _ __     ___ ___
            \\ \\ / __/ _` | '_ \   / __/ _ \\
            _\\ \\ (_| (_| | | | | |  (_|(_) |
            \\__/\\___\\__,_|_| |_|  \\___\\___(_)


    """)
    time.sleep(0.5)
    areasamount = random.randint(1,(scansize*syslvl))
    print("\t\t _______________________")
    areas = areasdef(areasamount,syslvl,intro)
    print("\t\t|_______________________|")
    #print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
    print("\n\nDo you wish to:\n\t1. scan a chosen object in more detail, for life signs, weaponry etc.\n\t2. Fly to the chosen object and prepare to dock/board/land.\n\t3. Exit Scanner")
    choice = input(": ")
    if(choice == "scan" or choice == "1" or choice == "one" or choice == "One" or choice == "Scan" or choice == "SCAN" or choice == "s" or choice == "S" or choice == "1."):
        print("Which object would you like to scan in detail? (full name or value)")
        choice = input(": ")
        #stuff here
    elif(choice == "2" or choice == "two" or choice == "Two" or choice == "Fly" or choice == "fly" or choice == "dock" or choice == "board"):
        print("Which object would you like to fly to? (full name or value)")
        choice = input(": ")
        #stuff here
def intro():
    clear(100)
    print("You are a ruthless mercenary, a soldier for hire (space pirate).\nYour mission: to reach the centre of the galaxy and discover what lies there.\nBut for now, think a little smaller, outside your window in the distance you see a small ship, some quick scans tell you there might be weapons aboard.\nBoard it kill any hostiles and leave with the weapons")
    input("Press enter to continue")
    clear(100)
    print("Type \"scan\" or \"s\" to scan for nearby objects in space")
    choice = input(": ")
    if(choice == "scan" or choice == "s" or choice == "Scan" or choice == "S" or choice == "SCAN"):
        scan(1,1,1)
    else:
        print("please type \"scan\" or \"s\"")
        time.sleep(1)
        intro()

print("Best viewed in fullscreen.")
time.sleep(1)
clear(100)
if(input("Do you wish to skip intro/tuorial? (y/n)") == "n"):
    intro()
