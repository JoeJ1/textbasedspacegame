import random
import time
import scan
import main

def clear(amount): #defining clear, a funcion which prints a certain amount of empty lines
    print("\n"*amount)

def marauder(syslvl,scanned,intro = 0):
    global areas
    clear(100)
    current = ""
    ships = ["","","","","","","","","","","","","","","","","","",""]
    a = 1
    print("""
               __  ___                           __                           ___    ____
              /  |/  /___ _ ____ ___ _ __ __ ___/ /___  ____ ___  ____  _  __<  /   |_  /
             / /|_/ // _ `// __// _ `// // // _  // -_)/ __// -_)/ __/ | |/ // /_  _/_ <
            /_/  /_/ \\_,_//_/   \\_,_/ \\_,_/ \\_,_/ \\__//_/   \\__//_/    |___//_/(_)/____/


    """)
    if(scanned == 0):
        print("Must scan for ships before running.")
    else:
        print("Which ship (no stations or unknown objects) do you wish to scan? (full name or value)")
        print("\t\t _______________________")
        while(a<=n):
            current = str(areas[a])
            if(current[:7] == "NEUTRAL" or current[:7] == "CORDIAL" or current[:7] == "HOSTILE"):
                ships[a] = areas[a]
                print("\t\t| ",a,str(ships[a]),"\t|")
            a = a +1
        if(intro == 1):
            clear(1)
            print("type the name of the ship")
        print("\t\t|_______________________|")
        choice = input(": ")
        if(str(choice) in ships):
            print("Worked!")
            #stuff here
        elif(choice.isdigit()):
            if(int(choice) < a):
                print("Worked!")
                print(str(ships[int(choice)]))
                #stuff here
