def var():
    global areas, scanned, notes, name, shipname, n, energy, area, x, y
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

    
def clear(amount):
    print("\n"*amount)
