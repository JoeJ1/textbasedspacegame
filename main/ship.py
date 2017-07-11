import var
import board
import time
import console


def clear(amount):
    print("\n"*amount)


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
        print("\"sanic\": does a heckin good fly.")
        print("\"exit\": closes smcs and returns to the ship's console.")
        smcs(0)
    elif(choice.lower() == "sanic"):
        print("Which object do you wish to travel to? (full name or value) type \"exit\", then \"list\" to see a list of scanned areas")
        choice = input(": ")
        if(choice.isdigit()):
            if(int(choice) <= var.n):
                var.area = str(var.areas[int(choice)])
                print("Do you wish to land at/dock with ", str(var.areas[int(choice)]), "? (y/n)")
                choice = input(": ")
                if(choice == "y"):
                    if(var.area[7] == "CORDIAL" or var.area[7] == "FRIENDLY" or var.area[7] == "NEUTRAL"):
                        board.shipboard()
                elif(choice == "n"):
                    print("Exiting to console...")
                    time.sleep(0.5)
                    console.console(1)
            else:
                print("That isn't one of the areas in this solar system.")
        else:
            if(choice in var.areas):
                var.area = str(choice)
    elif(choice == "clear"):
        clear(100)
    elif(choice == "exit"):
        console.console(1)
    smcs(0)
