def smcs():
    import var
    def smcs():
        print(""""
               _____ __  __  _____  _____
              / ____|  \/  |/ ____|/ ____|
             | (___ | \  / | |    | (___
              \___ \| |\/| | |     \___ \
              ____) | |  | | |____ ____) |
             |_____/|_|  |_|\_____|_____/
               Ship  Manual Control System

        """)
        i = 0
        print("\t\t_______________________")
        while(i<=len(var.areas)):
            print("\t\t|",i,". ",var.areas[i],"\t|")
            i = i +1
        print("\t\t|______________________|")
