import os
import sys
import random

def battle():
    os.system('cls')
    heroHealth = 20
    enemyHealth = 20

    while(heroHealth >= 1 or enemyHealth >= 1):
        print("Your Health:", heroHealth)
        print("Enemy Health:", enemyHealth)
        print("\n1) Attack")
        print("0) Exit")
        option = input("--> ")

        if option == "1":
            heroDamage = random.randint(0,10)
            print("\nYou dealt:", heroDamage, "damage!")
            enemyHealth -= heroDamage

            enemyDamage = random.randint(0,10)
            print("The enemy dealt:", enemyDamage, "damage!")
            heroHealth -= enemyDamage
            input()
            os.system('cls')

        elif option == "0":
            sys.exit()

        else:
            os.system('cls')
            battle()

    if(heroHealth <= 0):
        print("Your Health:", heroHealth)
        print("Enemy Health:", enemyHealth)
        print("\nYou lose!")
        print("You will now try again!")
        input()
        os.system('cls')
        battle()
    else:
        print("Your Health:", heroHealth)
        print("Enemy Health:", enemyHealth)
        print("\nYou win!")
        print("Now do it again!")
        input()
        os.system('cls')
        battle()

battle()
