import time
import scan
import marauder

def console(logo):
    global shellprompt
    if(logo == 1):
#        clear(100)
#        print("""
#                  _____  _____    _____  _    _    __      _____  _  _   ___
#         /\\      / ____||_   _|  / ____|| |  | |   \\ \\    / /__ \\| || | / _ \\
#        /  \\    | (___    | |   | (___  | |__| |    \\ \\  / /   ) | || || (_) |
#       / /\\ \\    \\___ \\   | |    \\___ \\ |  __  |     \\ \\/ /   / /|__   _\__, |
#      / ____ \\ _ ____) | _| |_ _ ____) || |  | |_     \\  /   / /_ _ | |   / /
#     /_/    \\_(_)_____(_)_____(_)_____(_)_|  |_(_)     \\/   |____(_)|_|  /_/
#
#     Advanced     Ship  Interactive    Shell          Version      2.49
#
#
#
#    """)
        print("Type \"help\" to view a list of commands")
        time.sleep(0.5)
        shellprompt = "[",name,"@",shipname," ~]$ "
        shellprompt = ''.join(shellprompt)
        su = 0
    choice = input(shellprompt)
    if(choice.lower() == "scan"):
        scan.scan(1,1,1)
    elif(choice == "marauder"):
        marauder.marauder(1,1)
    elif(choice == "help"):
        print("Advanced Ship Interactive Shell Version 2.49")
        print("Commands available:")
        print("scan: scans the area around your ship.")
        print("marauder: scans ships for loot, weapons and enemies.") #more commands here when implimented
        print("clear: clear the console")
    elif(choice == "su"):
        choice = input("Password: ")
        if(choice == "doggos"):
            shellprompt = "[name@shipname ~]# "
            su = 1
    elif(choice == "clear"):
        clear(50)
        time.sleep(0.1)
        clear(50)
    else:
        print("asish:",choice,": command not found")
    console(0)


def clear(amount): #defining clear, a funcion which prints a certain amount of empty lines
    print("\n"*amount)

# And so it begins
print("Best viewed in fullscreen.")
time.sleep(1)
clear(100)
name = input("What ur nam bro? ")
shipname = input("What that ship nam bro?")
if(input("Do you wish to skip intro/tuorial? (y/n)") == "n"): #deciding whether or not to call intro
    intro()#calling intro mission
else:
    clear(100)
    console(1)
