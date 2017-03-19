import os
import sys

class hero:
    def __init__(self, name):
        #Hero's name
        self.name = name
        #Level
        self.lvl = 1
        #Your maximum amount of health
        self.maxhealth = 100
        #Your current health (will change after a battle)
        self.health = self.maxhealth
        #Your maximum amount of stamina
        self.maxstamina = 20
        #Your current stamina
        self.stamina = self.maxstamina
        #Your maximum amount of maxstamina
        self.maxmana = 20
        #Your current mana
        self.mana = self.maxmana
        #Pysical Attack
        self.patk = 1
        #Magic Attack
        self.matk = 1
        #Physical Defense
        self.pdef = 1
        #Magic Defense
        self.mdef = 1
        #Strength
        self.strP = 0
        #Dexterity
        self.dexP = 0
        #Charisma
        self.chaP = 0
        #Intelligence
        self.intelP = 0
        #Intuition
        self.intuiP = 0
        #Vitality
        self.vitP = 0
        #Luck
        self.lukP = 0
        #Precision
        self.prcP = 0
        #Magic **RENAME**
        self.mgcP = 0
        #Atribute points available
        self.points = 20


def main():
    os.system('cls')
    print("Hello, what is your name?")
    option = input("--> ")
    #Makes heroIG able to be used anywhere
    global heroIG
    heroIG = hero(option)
    points()


def points():
    #Attributes do not yet give bonuses because we need to decide on them
    os.system('cls')
    print("Points available: ", heroIG.points)
    print("What would you like to level up:\n1.) Strength\n2.) Dexterity\n3.) Charisma\n4.) Intelligence\n5.) Intuition\n6.) Vitality\n7.) Luck\n8.) Precision\n9.) **Magic**\n\n0.) Exit\n\np.) Increase points\ns.) Stats")
    option = input('--> ')
    #Exit
    if option == "0":
        sys.exit()
    #0 or less than 0 points available
    elif heroIG.points <= 0:
        os.system('cls')
        print("You don't have enough points!")
        option = input('')
        points()

    #Strength
    elif option == "1":
        os.system('cls')
        #Will loop infinitely until a number is inputted.
        while True:
            try:
                print("Points Available: ", heroIG.points)
                print("How many points do you want to increase Strength by?")
                amtP = int(input('--> '))
                break
        #Insert string gives exception error. except will intercept it and it will continue to loop around.
            except:
                os.system('cls')

        if amtP <= heroIG.points:
            heroIG.strP += amtP
            heroIG.points -= amtP
            os.system('cls')
            print("You have increased Strength by", amtP,"points!")
            print("Points left:", heroIG.points)
            option = input('')
            points()
        else:
            os.system('cls')
            print("You don\'t have enough points!")
            option = input('')
            points()

    #Dexterity
    elif option == "2":
        os.system('cls')
        while True:
            try:
                print("Points Available: ", heroIG.points)
                print("How many points do you want to increase Dexterity by?")
                amtP = int(input('--> '))
                break
            except:
                os.system('cls')

        if amtP <= heroIG.points:
            heroIG.dexP += amtP
            heroIG.points -= amtP
            os.system('cls')
            print("You have increased Dexterity by", amtP,"points!")
            print("Points left:", heroIG.points)
            option = input('')
            points()
        else:
            os.system('cls')
            print("You don\'t have enough points!")
            option = input('')
            points()

    #Charisma
    elif option == "3":
        os.system('cls')
        while True:
            try:
                print("Points Available: ", heroIG.points)
                print("How many points do you want to increase Charisma by?")
                amtP = int(input('--> '))
                break
            except:
                os.system('cls')

        if amtP <= heroIG.points:
            heroIG.chaP += amtP
            heroIG.points -= amtP
            os.system('cls')
            print("You have increased Charisma by", amtP,"points!")
            print("Points left:", heroIG.points)
            option = input('')
            points()
        else:
            os.system('cls')
            print("You don\'t have enough points!")
            option = input('')
            points()

    #Intelligence
    elif option == "4":
        os.system('cls')
        while True:
            try:
                print("Points Available: ", heroIG.points)
                print("How many points do you want to increase Intelligece by?")
                amtP = int(input('--> '))
                break
            except:
                os.system('cls')

        if amtP <= heroIG.points:
            heroIG.intelP += amtP
            heroIG.points -= amtP
            os.system('cls')
            print("You have increased Intelligence by", amtP,"points!")
            print("Points left:", heroIG.points)
            option = input('')
            points()
        else:
            os.system('cls')
            print("You don\'t have enough points!")
            option = input('')
            points()
    #Intuition
    elif option == "5":
        os.system('cls')
        while True:
            try:
                print("Points Available: ", heroIG.points)
                print("How many points do you want to increase Intuition by?")
                amtP = int(input('--> '))
                break
            except:
                os.system('cls')

        if amtP <= heroIG.points:
            heroIG.intuiP += amtP
            heroIG.points -= amtP
            os.system('cls')
            print("You have increased Intuition by", amtP,"points!")
            print("Points left:", heroIG.points)
            option = input('')
            points()
        else:
            os.system('cls')
            print("You don\'t have enough points!")
            option = input('')
            points()
    #Vitality
    elif option == "6":
        os.system('cls')
        while True:
            try:
                print("Points Available: ", heroIG.points)
                print("How many points do you want to increase Vitality by?")
                amtP = int(input('--> '))
                break
            except:
                os.system('cls')

        if amtP <= heroIG.points:
            heroIG.vitP += amtP
            heroIG.points -= amtP
            os.system('cls')
            print("You have increased Vitality by", amtP,"points!")
            print("Points left:", heroIG.points)
            option = input('')
            points()
        else:
            os.system('cls')
            print("You don\'t have enough points!")
            option = input('')
            points()
    #Luck
    elif option == "7":
        os.system('cls')
        while True:
            try:
                print("Points Available: ", heroIG.points)
                print("How many points do you want to increase Luck by?")
                amtP = int(input('--> '))
                break
            except:
                os.system('cls')

        if amtP <= heroIG.points:
            heroIG.lukP += amtP
            heroIG.points -= amtP
            os.system('cls')
            print("You have increased Luck by", amtP,"points!")
            print("Points left:", heroIG.points)
            option = input('')
            points()
        else:
            os.system('cls')
            print("You don\'t have enough points!")
            option = input('')
            points()
    #Precision
    elif option == "8":
        os.system('cls')
        while True:
            try:
                print("Points Available: ", heroIG.points)
                print("How many points do you want to increase Precision by?")
                amtP = int(input('--> '))
                break
            except:
                os.system('cls')

        if amtP <= heroIG.points:
            heroIG.prcP += amtP
            heroIG.points -= amtP
            os.system('cls')
            print("You have increased Precision by", amtP,"points!")
            print("Points left:", heroIG.points)
            option = input('')
            points()
        else:
            os.system('cls')
            print("You don\'t have enough points!")
            option = input('')
            points()
    #Magic **RENAME**
    elif option == "9":
        os.system('cls')
        while True:
            try:
                print("Points Available: ", heroIG.points)
                print("How many points do you want to increase Magic by?")
                amtP = int(input('--> '))
                break
            except:
                os.system('cls')

        if amtP <= heroIG.points:
            heroIG.mgcP += amtP
            heroIG.points -= amtP
            os.system('cls')
            print("You have increased Magic by", amtP,"points!")
            print("Points left:", heroIG.points)
            option = input('')
            points()
        else:
            os.system('cls')
            print("You don\'t have enough points!")
            option = input('')
            points()
    #View your stats
    elif option == "s":
        stats()
    #Add points
    elif option == "p":
        heroIG.points += 1
        points()
    else:
        os.system('cls')
        points()


def stats():
    #Shows your stats
    os.system('cls')
    print("Stats:\n")
    print("Name: %s" % heroIG.name)
    print("Health: %i/%i" % (heroIG.health, heroIG.maxhealth))
    print("Stamina: %i/%i" % (heroIG.stamina, heroIG.maxstamina))
    print("Mana: %i/%i" % (heroIG.mana, heroIG.maxmana))
    print("Physical Attack: %i" % heroIG.patk)
    print("Physical Defense: %i" % heroIG.pdef)
    print("Magic Attack: %i" % heroIG.matk)
    print("Magic Defense: %i" % heroIG.mdef)
    print("Strength: %i" % heroIG.strP)
    print("Dexterity: %i" % heroIG.dexP)
    print("Charisma: %i" % heroIG.chaP)
    print("Intelligence: %i" % heroIG.intelP)
    print("Intuition: %i" % heroIG.intuiP)
    print("Vitality: %i" % heroIG.vitP)
    print("Luck: %i" % heroIG.lukP)
    print("Precision: %i" % heroIG.prcP)
    print("**Magic**: %i" % heroIG.mgcP)
    print("")
    print("p.) Points\n0.) Exit\n")
    option = input('--> ')
    #Return to points
    if option == "p":
        points()
    #Exit
    elif option == "0":
        sys.exit()
    else:
        stats()




main()

