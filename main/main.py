import time #importing time, an external package.
import intro #importing intro, console and var, files made for this game.
import console# ""
import var# ""


def clear(amount, version = 0, speed = 0.02): #Defining clear, a function which prints an amount of blank space.
    if(version == 0): #version 0, the default clear version, clears all lines at once.
        print("\n"*amount)
    elif(version == 1): #version 1 prints with a while loop, one line at a time but as quickly as your computer can handle it.
        i = 0
        while(i<amount):
            print("\n")
    elif(version == 2): #version 2 prints with a while loop but with a pause between each line (determined by the third paramater of the function).
        i = 0
        while(i<amount):
            time.sleep(speed)
            print("\n")
# And so it begins
print("Best viewed in fullscreen.")
var.var() #calling var, a function within the file var.
time.sleep(1) #waiting for one second for the user to read the previous message.
clear(100) #clearing the console.
var.name = input("What is your name, mercenary? ") #setting the name variable to whatever the user wants.
var.shipname = input("What is the name of your trusty ship? ") #setting the shipname variable to whatever the user wants.
if(input("Do you wish to skip intro/tutorial? (y/n)") == "n"): #calling intro if the player wants to play the intro.
    intro.intro()# ""
else: #otherwise, booting straight into the game.
    clear(100)# ""
    console.console(1)# ""
