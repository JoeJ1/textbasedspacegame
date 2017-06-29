import random
def shipgen(sizex,sizey):
    array = ["",]*sizey*sizex
    i = 0
    while(i<len(array)):
        array[i] = random.randint(0,2)
        i = i+1
    array[0] = 1
    string = ','.join(str(array))
    string = string.replace("[","")
    string = string.replace("]","")
    string = string.replace(",","")
    string = string.replace(" ","")
    string = [string[a:a+sizey] for a in range(0, len(string), sizey)]
