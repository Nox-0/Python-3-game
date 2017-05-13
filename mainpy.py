import sys
import os
import pickle



def main():
    os.system('cls')
    print("Welcome to my game!\n")
    print("1.) Start")
    print("2.) Load")
    print("0.) Exit")
    option = input("--> ")
    if option == "1":
        import startpy
        startpy.start()
    elif option == "2":
        if os.path.exists("savefile") == True:
            os.system('cls')
            with open('savefile', 'rb') as f:
                global heroP
                heroP = pickle.load(f)
            print("Loaded Save State...")
            option = input()
            menu1py.menu1()
        else:
            print("You have no save file for this game.")
            option = input()
            main()
    elif option == "0":
        sys.exit()
    else:
        main()

main()
