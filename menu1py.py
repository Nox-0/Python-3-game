import sys
import os
import pickle




def menu1():
    os.system('cls')
    print("1.) Fight\n2.) Store\n3.) Save\n4.) Stats\n5.) Inventory\n6.) Level Points\n0.) Back")
    option = input("--> ")
    if option == "1":
        pass
    elif option == "2":
        pass
    elif option == "3":
        os.system('cls')
        with open('savefile', 'wb') as f:
            pickle.dump(PlayerIG, f)
            print("\nGame has been saved!\n")
        option = input('')
        pass
    elif option == "4":
        pass
    elif option == "5":
        pass
    elif option == "6":
        pass
    elif option == "0":
        import mainpy
        mainpy.main()
    else: menu1()
