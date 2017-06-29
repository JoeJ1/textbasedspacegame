import random
import time
import console
import var


def clear(amount):
    print("\n"*amount)


def scan(logo):
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
    choice = input("(scan) ")
    if(choice == "wscan"):
        wscan(1, 1)
    elif(choice.lower() == "help"):
        print("\nwscan: do a wide scan of the local solar system")
        print("dscan: do a detailed scan of a specific location")
        print("exit: exit scan and return to shell")
        print("clear: clear the console")
    elif(choice == "dscan"):  # processing input
        dscan(1, 1)
    elif(choice == "exit"):
        console.console(1)
    elif(choice == "clear"):
        clear(100)
    else:
        print("scan:", choice, ": command not found")
    scan(0)


def dscan(syslvl, scanned):
    global areas, n
    clear(100)
    current = ""
    ships = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    a = 1
    if(var.scanned == 0):
        print("Must scan for ships before running.")
    else:
        print("Which ship (no stations or unknown objects) do you wish to scan? (full name or value)")
        print("\t\t _______________________")
        while(a <= n):
            current = str(var.areas[a])
            if(current[:7] == "NEUTRAL" or current[:7] == "CORDIAL" or current[:7] == "HOSTILE"):
                ships[a] = var.areas[a]
                print("\t\t| ", a, str(ships[a]), "\t|")
            a = a + 1
        print("\t\t|_______________________|")
        choice = input(": ")
        if(str(choice) in ships):
            print("Scanning...")
            time.sleep(2)
            print("Worked!")
            # stuff here
        elif(choice.isdigit()):
            if(int(choice) < a):
                print("Scanning...")
                time.sleep(2)
                print("Worked!")
                print(str(ships[int(choice)]))
                # stuff here


def wscan(syslvl, scansize):
    global areas, scanned, i, n
    areasamount = random.randint(1, (scansize*syslvl))
    print("Scanning...")
    time.sleep(2)
    print("Found", areasamount, "points of intrest. ")
    print("\t\t _______________________")  # the box around the objects displayed in the scanner
    if(var.scanned == 0):
        areasdef(areasamount, syslvl)
        var.scanned = 1
    else:
        i = 1
        while(i <= n):
            print("\t\t| ", i, ". ", str(var.areas[i]), "\t|")
            i = i + 1
    print("\t\t|_______________________|")  # the bottom half of the box around objects in the scanner
