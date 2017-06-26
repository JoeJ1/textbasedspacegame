def scan(syslvl,scansize,intro = 0): #intro should be whether or not this is the scan in the intro (1 if it is 0 if it's not)
    global n, areas, scanned
    clear(100) #100 lines of nothing
    print("""
           _____                        ____  _  _  __
          / ____|                      |___ \\| || |/_ |
         | (___   ___ __ _ _ __   __   ____) | || |_| |
          \\___ \\ / __/ _` | '_ \\  \\ \\ / /__ <|__   _| |
          ____) | (_| (_| | | | |  \\ V /___) |  | | | |
         |_____/ \\___\\__,_|_| |_|   \\_/|____(_) |_| |_|
    """)
    time.sleep(0.5)
    areasamount = random.randint(1,(scansize*syslvl))
    print("\t\t _______________________") #the box around the objects displayed in the scanner
    if(scanned == 0):
        areasdef(areasamount,syslvl,intro)
        scanned = 1
    else:
        i = 1
        while(i<=n):
            print("\t\t| ",i,". ",str(areas[i]),"\t|")
            i= i+1

    print("\t\t|_______________________|") # the bottom half of the box around objects in the scanner
    #print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
    print("\nType \"h\" to show help.")
    choice = input(": ") # taking input from player
    if(choice == "h" or choice == "help" or choice == "H" or choice == "Help" or choice == "HELP"):
        print("\n\nDo you wish to:\n\t1. scan a chosen object in more detail, for life signs, weaponry etc.\n\t2. Fly to the chosen object and prepare to dock/board/land.\n\t3. Exit Scanner")
        choice = input(":")
        if(choice == "scan" or choice == "1" or choice == "one" or choice == "one" or choice == "scan" or choice == "scan" or choice == "s" or choice == "s" or choice == "1k."): #processing input
            print("this will exit scan and take you to marauderer. confirm (y =leave/n = stay)")
            choice = input(": ")
            if(choice == "y"):
                marauderer(syslvl,scanned,intro)
            else:
                scan(syslvl,scansize,intro)
                #stuff here
        elif(choice == "2" or choice == "two" or choice == "Two" or choice == "Fly" or choice == "fly" or choice == "dock" or choice == "board"):
            print("Which object would you like to fly to? (full name or value)")
            choice = input(": ")
            #stuff here
    if(choice == "scan" or choice == "1" or choice == "one" or choice == "one" or choice == "scan" or choice == "scan" or choice == "s" or choice == "s" or choice == "1k."): #processing input
        print("this will exit scan and take you to marauderer. confirm (y =leave/n = stay)")
        choice = input(": ")
        if(choice == "y"):
            marauderer(syslvl,scanned,intro)
        else:
            scan(syslvl,scansize,intro)
            #stuff here
    elif(choice == "2" or choice == "two" or choice == "Two" or choice == "Fly" or choice == "fly" or choice == "dock" or choice == "board"):
        print("Which object would you like to fly to? (full name or value)")
        choice = input(": ")
        #stuff here
