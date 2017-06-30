import random
import time
import console
import var
import lvlgen


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
    elif(choice == "dscan"):

        dscan(1, 1)
    elif(choice == "exit"):
        console.console(1)
    elif(choice == "clear"):
        clear(100)
    else:
        print("scan:", choice, ": command not found")
    scan(0)


def dscan(syslvl, scanned):
    global areas
    clear(100)
    print("How much energy would you like to use to scan for objects?\n (You have", var.energy, "remaining)")
    choice = input(": ")
    if(choice == int() and choice < (var.energy - 10)):
        var.energy = var.energy - (choice)
        scandetail = choice
    else:
        print("That's not a number or you dont have enough energy.")
    if(var.scanned == 0):
        print("Must run a wide scan before running.")
    else:
        print("What do you wish to scan? (Enter value of object)")
        print("\t\t _______________________")
        i = 1
        while(i <= var.n):
            print("\t\t| ", i, ". ", str(var.areas[i]), "\t|")
            i = i + 1
        print("\t\t|_______________________|")
        choice = input(": ")
        if(choice == scandetail):
            print("wip")


def wscan(syslvl, scansize):
    global areas, scanned, i
    areasamount = random.randint(1, (scansize*syslvl))
    if(scanned == 0):
        print("Scanning...")
        time.sleep(2)
    print("Found", areasamount, "points of intrest: ")
    print("\t\t _______________________")  # the box around the objects displayed in the scanner
    if(var.scanned == 0):
        lvlgen.areasdef(areasamount, syslvl)
        var.scanned = 1
    else:
        i = 1
        while(i <= var.n):
            print("\t\t| ", i, ". ", str(var.areas[i]), "\t|")
            i = i + 1
    print("\t\t|_______________________|")  # the bottom half of the box around objects in the scanner
