import time
from main import *
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
        shellprompt = "[",name.lower(),"@",shipname.lower()," ~]$ "
        shellprompt = ''.join(shellprompt)
        su = 0
    choice = input(shellprompt)
    if(choice.lower() == "scan"):
        scan.scan(1,1,1)
    elif(choice == "help"):
        print("Advanced Ship Interactive Shell Version 2.49")
        print("Commands available:")
        print("scan: scans the area around your ship.")
        print("clear: clear the console")
    elif(choice == "su" and su == 0):
        choice = input("Password: ")
        if(choice == "doggos"):
            shellprompt = "[",name.lower(),"@",shipname.lower()," ~]# "
            shellprompt = ''.join(shellprompt)
            su = 1
        else:
            print("na")
    elif(choice == "clear"):
        clear(50)
        time.sleep(0.1)
        clear(50)
    elif(choice == "exit" and su == 1):
        shellprompt = "[",name.lower(),"@",shipname.lower()," ~]$ "
        shellprompt = ''.join(shellprompt)
        su = 0
        clear(50)
        time.sleep(0.1)
        clear(50)
    else:
        print("asish:",choice,": command not found")
    console(0)
