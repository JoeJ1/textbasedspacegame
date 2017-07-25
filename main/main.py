import time #importing time, an external package.
import intro #importing intro, console and var, files made for this game.
import console# ""
import var# ""

# And so it begins
print("Best viewed in fullscreen.")
var.var() #calling var, a function within the file var.
time.sleep(1) #waiting for one second for the user to read the previous message.
var.clear(100) #clearing the console.
var.name = input("What is your name, mercenary? ") #setting the name variable to whatever the user wants.
var.shipname = input("What is the name of your trusty ship? ") #setting the shipname variable to whatever the user wants.
if(input("Do you wish to skip intro/tutorial? (y/n)") == "n"): #calling intro if the player wants to play the intro.
    intro.intro()# ""
else: #otherwise, booting straight into the game.
    var.clear(100)# ""
    console.console(1)# ""
