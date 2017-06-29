import time
import scan
import var
import ship


def console(logo):
    global shellprompt, su
    if(logo == 1):
        print("Type \"help\" to view a list of commands")
        time.sleep(0.5)
        shellprompt = "[", var.name.lower(), "@", var.shipname.lower(), " ~]$"
        shellprompt = ''.join(shellprompt)
        shellprompt = shellprompt.replace(" ", "")
        shellprompt = shellprompt+" "
        su = 0
    choice = input(shellprompt)
    if(choice.lower() == "scan"):
        scan.scan(1)
    elif(choice == "notes"):
        print(var.notes)
        var.notes = "\n", str(var.notes)+str(input("What do you want to add to your notes? "))+""
    elif(choice == "help"):
        print("\nAdvanced Ship Interactive Shell Version 2.49")
        print("Commands available:")
        print("scan: scans the area around your ship.")
        print("clear: clear the console")
        print("smcs: ship manual control system; allows you to pilot your ship or set autopilot")
    elif(choice == "su" and su == 0):
        choice = input("Password: ")
        if(choice == "doggos"):
            shellprompt = "[", var.name.lower(), "@", var.shipname.lower(), " ~]#"
            shellprompt = ''.join(shellprompt)
            shellprompt = shellprompt.replace(" ", "")
            shellprompt = shellprompt+" "
            su = 1
        else:
            print("na")
    elif(choice == "clear"):
        clear(50)
        time.sleep(0.1)
        clear(50)
    elif(choice == "exit" and su == 1):
        shellprompt = "[", var.name.lower(), "@", var.shipname.lower(), " ~]$ "
        shellprompt = ''.join(shellprompt)
        su = 0
        clear(50)
        time.sleep(0.1)
        clear(50)
    elif(choice == "smcs"):
        ship.smcs()
    else:
        print("asish:", choice, ": command not found")
    console(0)


def clear(amount):  # defining clear, a funcion which prints a certain amount of empty lines
    print("\n"*amount)
