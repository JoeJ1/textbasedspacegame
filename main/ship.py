import var
import board
import time
import random
import console


def flyingflavourtext():
    var.clear(100)
    print("Ship in transport. Please wait...")
    time.sleep(0.5)
    var.clear(100)
    print("Ship in transport. Please wait...\nStarting engines...")
    time.sleep(1)
    var.clear(100)
    print("Ship in transport. Please wait...\nOrienting towards target...")
    time.sleep(1)
    i = 0
    while(i < 299792458):
        var.clear(100)
        print("Ship in transport. Please wait...\nAccellorating towards target speed of 299 792 458 ms\u207b\u00b9...\nCurrent speed :", i, "ms\u207b\u00b9")
        i = i + 299792.45
        time.sleep(0.01)
    j = random.randint(30000000000, 9999999999999)
    i = j
    while(i > 0):
        var.clear(100)
        print("Ship in transport. Please wait...\nDistance from target: ", i, "\nCurrent speed: ", random.choice(["299 792 458 ms\u207b\u00b9", "299 792 457 ms\u207b\u00b9", "299 792 456 ms\u207b\u00b9"]))
        i = i - j/100
        time.sleep(0.1)
    var.clear(100)
    print("Destination reached. Prepare to disembark.")
    time.sleep(1)


def smcs(logo=1):
    if(logo == 1):
        print("""
               _____ __  __  _____  _____
              / ____|  \\/  |/ ____|/ ____|
             | (___ | \\  / | |    | (___
              \\___ \\| |\/| | |     \___ \\
              ____) | |  | | |____ ____) |
             |_____/|_|  |_|\\_____|_____/
               Ship  Manual Control System
            """)
    print("Type \"help\" for a list of commands")  # smcs is a program which flies to areas in the solar system
    choice = input("(smcs) ")
    if(choice.lower() == "list"):
        if(var.scanned == 1):
            print("\t\t _______________________")
            i = 1
            while(i <= var.n):
                print("\t\t|", i, ". ", var.areas[i], "\t|")
                i = i + 1
            print("\t\t|_______________________|")
        else:
            print("Error: please scan star system before running.")
    elif(choice.lower() == "help"):
        print("Commands available: ")
        print("\"list\": lists the known objects in the current star system. (returns error if scan has not been run)")
        print("\"fly\": automatically transports the ship to a desired location.")
        print("\"exit\": closes smcs and returns to the ship's console.")
        smcs(0)
    elif(choice.lower() == "fly"):
        print("Which object do you wish to travel to? (full name or value) type \"exit\", then \"list\" to see a list of scanned areas")
        choice = input(": ")
        if(choice.isdigit()):
            if(int(choice) <= var.n):
                var.area = str(var.areas[int(choice)])
                print("Do you wish to land at/dock with ", str(var.areas[int(choice)]), "? (y/n)")
                choice = input(": ")
                if(choice == "y"):
                    flyingflavourtext()
                    if(var.area[7] == "CORDIAL" or var.area[7] == "FRIENDLY" or var.area[7] == "NEUTRAL"):
                        board.shipboard()
                    elif(var.area[7] == "UNKOWN"):
                        board.unkownboard()
                    elif(var.area[7] == "STATION"):
                        board.stationboard()
                elif(choice == "n"):
                    print("Exiting to console...")
                    time.sleep(0.5)
                    console.console(1)
            else:
                print("That isn't one of the areas in this solar system.")
        else:
            if(choice in var.areas):
                var.area = str(choice)
                print("Do you wish to land at/dock with ", str(var.area), "? (y/n)")
                choice = input(": ")
                if(choice == "y"):
                    flyingflavourtext()
                    if(var.area[7] == "CORDIAL" or var.area[7] == "FRIENDLY" or var.area[7] == "NEUTRAL"):
                        board.shipboard()
                    elif(var.area[7] == "UNKNOWN"):
                        board.unknownboard()
                    elif(var.area[7] == "STATION"):
                        board.stationboard()
                    # elif()
                elif(choice == "n"):
                    print("Exiting to console...")
                    time.sleep(0.5)
                    console.console(1)
            else:
                print("That isn't one of the areas in this solar system.")
    elif(choice == "clear"):
        var.clear(100, 3)
    elif(choice == "exit"):
        console.console(1)
    smcs(0)
