import time
import scan
import var

def console(logo):
    global shellprompt, su
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
        shellprompt = "[",var.name,"@",var.shipname,"]$ "
        shellprompt = ''.join(shellprompt)
        su = 0
    choice = input(shellprompt)
    if(choice.lower() == "scan"):
        scan.scan(1)
    elif(choice == "help"):
        print("\nAdvanced Ship Interactive Shell Version 2.49")
        print("Commands available:")
        print("scan: scans the area around your ship.")
        print("clear: clear the console")
    elif(choice == "su" and su == 0):
        choice = input("Password: ")
        if(choice == "doggos"):
            shellprompt = "[",var.name,"@",var.shipname,"]# "
            shellprompt = ''.join(shellprompt)
            su = 1
        else:
            print("na")
    elif(choice == "clear"):
        clear(50)
        time.sleep(0.1)
        clear(50)
    elif(choice == "exit" and su == 1):
        shellprompt = "[",var.name.lower(),"@",var.shipname.lower()," ~]$ "
        shellprompt = ''.join(shellprompt)
        su = 0
        clear(50)
        time.sleep(0.1)
        clear(50)
    else:
        print("asish:",choice,": command not found")
    console(0)

def clear(amount): #defining clear, a funcion which prints a certain amount of empty lines
    print("\n"*amount)
