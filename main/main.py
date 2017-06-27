import time
import scan
import marauder

def console(logo):
    global shellprompt
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
        print("Type \"help\" to view help or \"cmds\" to view commands.")
        time.sleep(0.5)
        shellprompt = "[name@shipname ~]$ "
    choice = input(shellprompt)
    if(choice.lower() == "scan"):
        scan.scan(1,1)
    elif(choice == "marauder"):
        marauder.marauder(1,1)
    elif(choice.lower() == "help"):
        print("Format:") #used seperate prints to make it easier to read when editing (can easily be changed in the future)
        print("command_name -alternate_option (what to type) : description (what it does)")
    elif(choice == "cmds"):
        print("Commands available:")
        clear(1)
        print("scan: scans the area around your ship.")
        clear(1)
        print("marauder: scans ships for loot, weapons and enemies.") #more commands here when implimented
    elif(choice == "su"):
        choice = input("Password: ")
        if(choice == "doggos"):
            shellprompt = "[name@shipname ~]# "
            su = 1
    else:
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
