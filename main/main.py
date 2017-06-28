import time
import scan
import intro
import console

def clear(amount): #defining clear, a funcion which prints a certain amount of empty lines
    print("\n"*amount)

# And so it begins
print("Best viewed in fullscreen.")
log = open("log.txt", "w")
time.sleep(1)
clear(100)
name = input("What is your name, mercenary? ")
shipname = input("What is the name of your trusty ship? ")
if(input("Do you wish to skip intro/tutorial? (y/n)") == "n"): #deciding whether or not to call intro
    intro #calling intro mission
else:
    clear(100)
    console.console(1)
