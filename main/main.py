import time
import random
import scan as scan
import marauder as marauder
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

def console(logo):
    if(logo == 1):
        clear(100)
        print("""
                  _____  _____    _____  _    _    __      _____  _  _   ___
         /\\      / ____||_   _|  / ____|| |  | |   \\ \\    / /__ \\| || | / _ \\
        /  \\    | (___    | |   | (___  | |__| |    \\ \\  / /   ) | || || (_) |
       / /\\ \\    \\___ \\   | |    \\___ \\ |  __  |     \\ \\/ /   / /|__   _\__, |
      / ____ \\ _ ____) | _| |_ _ ____) || |  | |_     \\  /   / /_ _ | |   / /
     /_/    \\_(_)_____(_)_____(_)_____(_)_|  |_(_)     \\/   |____(_)|_|  /_/

     Advanced     Ship  Interactive    Shell          Version      2.49


    """)
    time.sleep(0.5)
    print("Type \"help\" to view help or \"cmds\" to view commands.")
    shellprompt = "[name@shipname]$ "
    choice = input(shellprompt)
    if(choice.lower() == "scan"):
        scan.scan()
    elif(choice.lower() == "help"):
        clear(5)
        print("Format:") #used seperate prints to make it easier to read when editing (can easily be changed in the future)
        print("command_name -alternate_option (what to type) : description (what it does)")
    elif(choice == "cmds"):
        clear(5)
        print("Commands available:")
        clear(1)
        print("scan: scans the area around your ship.")
        clear(1)
        print("marauderer: scans ships for loot, weapons and enemies.") #more commands here when implimented
    elif(choice == "su"):
        clear(5)
        shellprompt = "[name@shipname]# "
    else:
        clear(5)
        print("asish:",choice,": command not found")
    console(0)


def clear(amount): #defining clear, a funcion which prints a certain amount of empty lines
    print("\n"*amount)

print("Best viewed in fullscreen.")
time.sleep(1)
clear(100)
if(input("Do you wish to skip intro/tuorial? (y/n)") == "n"): #deciding whether or not to call intro
    intro()#calling intro mission
else:
    console(1)
