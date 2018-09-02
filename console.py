import time  # importing time
import scan  # importing necissarry files, as usual.
import var  # git test_
import ship


def console(logo=1):  # The console, where the player can type commands to use the ship in different ways.
    global shellprompt  # globalising shellprompt
    if(logo == 1):  # logo should be whether or not the console logo is displayed but currently is not in use.
        print("Type \"help\" to view a list of commands")
        var.su = 0  # defining su (super user) variable 0 = disabled; 1 = enabled
        time.sleep(0.5)  # waiting...
        var.shellprompt = var.BOLD, var.GREEN, "[", var.name.lower().replace(" ", ""), "@", var.shipname.lower().replace(" ", ""), var.WHITE, var.BOLD, var.folder, var.GREEN, "]$ ", var.WHITE  # defining shellprompt.
        var.shellprompt = ''.join(var.shellprompt)  # fixing visual shellprompt issues
    choice = input(var.shellprompt)  # getting the user's input and storing it as choice
    if(choice.lower() == "scan"):  # calling the scan function within the scan file upon the user's input
        scan.scan(1)
    elif(choice == "notes"):  # showing the notes of the user and allowing them to add any if they please.
        print(var.notes)
        var.notes = "\n", str(var.notes)+str(input("What do you want to add to your notes? "))+""
    elif(choice == "help"):  # Displaying a help message, with a list of commands.
        print("\nAdvanced Ship Interactive Shell Version 2.49\n")
        print("Format: <command>: <description of command>  (type the command exactly as it is written.)\n")
        print("Commands available:")
        print(" scan: scans the area around your ship.")
        print(" clear: clear the console.")
        print(" smcs: ship manual control system; allows you to pilot your ship or set autopilot.")
        print(" su: enables super user, adding extra functionality and permissions. Requires password.")
        print(" exit: disables super user if currently enabled.")
    elif(choice == "su" and var.su == 0):  # enabling super user if the player has the correct password.
        choice = input("Password: ")
        if(choice == "doggos"):  # placeholder password
            var.shellprompt = "[", var.name.lower(), "@", var.shipname.lower(), " ~]#"  # changing the look of the prompt when super user is enabled.
            var.shellprompt = ''.join(var.shellprompt)  # fixing visual shellprompt issues.
            var.shellprompt = var.shellprompt.replace(" ", "")
            var.shellprompt = var.shellprompt+" "
            var.su = 1
        else:
            print("Incorrect password. Access Denied.")  # If the password is incorrect then
    elif(choice == "clear"):  # similar to the clear function but waits for a tenth of a second inbetween printing 50 lines twice (100 lijnes total) The pause makes the clearing animation feel more natural.
        var.clear(100, 3)
    elif(choice == "exit" and var.su == 1):  # exiting super user if the player chooses.
        var.shellprompt = "[", var.name.lower(), "@", var.shipname.lower(), " ~]$ "  # resetting prompt to normal.
        var.shellprompt = ''.join(var.shellprompt)  # fixing shellprompt visual issues.
        var.su = 0  # disabling super user
        var.clear(100, 3)
    elif(choice == "smcs"):  # calling "SMCS" -ship manual control systems
        ship.smcs()
    else:
        print("asish:", choice, ": command not found")  # printing an error message if no command is found
    console(0)  # calling the console function again (repeating all previous code.)
