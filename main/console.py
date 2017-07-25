import time #importing time
import scan #importing necissarry files, as usual.
import var  # ""
import ship # ""


def console(logo = 1): #The console, where the player can type commands to use the ship in different ways.
    su = 0 # defining su (super user) variable 0 = disabled; 1 = enabled
    if(logo == 1): #logo should be whether or not the console logo is displayed but currently is not in use.
        print("Type \"help\" to view a list of commands")
        time.sleep(0.5) #waiting...
        shellprompt = "[", var.name.lower(), "@", var.shipname.lower(), " ~]$" #defining shellprompt.
        shellprompt = ''.join(shellprompt) #fixing shellprompt issues
        shellprompt = shellprompt.replace(" ", "")# ""
        shellprompt = shellprompt+" " #" "
    choice = input(shellprompt)#getting the user's input and storing it as choice
    if(choice.lower() == "scan"): #calling the scan function within the scan file upon the user's input
        scan.scan(1)# ""
    elif(choice == "notes"): #showing the notes of the user and allowing them to add any if they please.
        print(var.notes) # ""
        var.notes = "\n", str(var.notes)+str(input("What do you want to add to your notes? "))+"" #""
    elif(choice == "help"): #Displaying a help message, with a list of commands.
        print("\nAdvanced Ship Interactive Shell Version 2.49") # ""
        print("Commands available:")  # ""
        print("scan: scans the area around your ship.") #""
        print("clear: clear the console")# ""
        print("smcs: ship manual control system; allows you to pilot your ship or set autopilot") #""
    elif(choice == "su" and su == 0): #enabling super user if the player has the correct password.
        choice = input("Password: ")
        if(choice == "doggos"): #placeholder password
            shellprompt = "[", var.name.lower(), "@", var.shipname.lower(), " ~]#"
            shellprompt = ''.join(shellprompt)
            shellprompt = shellprompt.replace(" ", "")
            shellprompt = shellprompt+" "
            su = 1
        else:
            print("Incorrect password. Access Denied.")
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
