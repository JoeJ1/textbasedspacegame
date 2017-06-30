import var


def smcs():
    print(""""
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
    elif(choice.lower() == "sanic"):
        print("Which object do you wish to travel to? (full name or value) type \"exit\", then \"list\" to see a list of scanned areas")
        choice = input(": ")
        if(choice.isdigit()):
            if(choice <= var.n):
                var.area = str(var.areas[int(choice)])
            else:
                print("That isn't one of the areas in this solar system.")
        else:
            if(choice in var.areas):
                var.area = str(choice)
