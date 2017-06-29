import time
import intro
import console
import var


def clear(amount):
    print("\n"*amount)


# And so it begins
print("Best viewed in fullscreen.")
var.var()
time.sleep(1)
clear(100)
var.name = input("What is your name, mercenary? ")
var.shipname = input("What is the name of your trusty ship? ")
if(input("Do you wish to skip intro/tutorial? (y/n)") == "n"):
    intro.intro()
else:
    clear(100)
    console.console(1)
