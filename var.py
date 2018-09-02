import time
# import random


def var():
    global areas, scanned, notes, name, shipname, n, energy, area, x, y, areatype, objects, areamap, shellprompt, su, END, BOLD, WHITE, RED, GREEN, ORANGE, BLUE, PURPLE, folder
    areas = ["", "", "", "", "", "", "", "", "", ""]
    scanned = 0
    name = ""
    shipname = ""
    notes = ""
    n = 0
    energy = 100
    area = ""
    areatype = ""
    areamap = [""]
    x = 0
    y = 0
    objects = [""]
    shellprompt = ""
    su = 0
    folder = " ~"
    WHITE = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[92m'
    ORANGE = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    BOLD = '\033[1m'
    END = '\033[0m'


def clear(amount, version=0, speed=0.1, chunksize=50):  # Defining clear, a function which prints an amount of blank space.
    if(version == 0):  # version 0, the default clear version, clears all lines at once.
        print("\n"*amount)
    elif(version == 1):  # version 1 prints with a while loop, one line at a time but as quickly as your computer can handle it.
        i = 0
        while(i < amount):
            print("\n")
    elif(version == 2):  # version 2 prints with a while loop but with a pause between each line (determined by the third paramater of the function).
        i = 0
        while(i < amount):
            time.sleep(speed)
            print("\n")
    elif(version == 3):  # vesion 3 prints chunks of lines with a pause inbetween each chunk
        i = 0
        while(i < amount):
            time.sleep(speed)
            print("\n"*chunksize)
            i = i + chunksize
