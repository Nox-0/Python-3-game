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
        self.lucP = 0
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
        heroIG.strP += 1
        heroIG.points -= 1
        print("You have increased Strength!")
        option = input('')
        points()
    #Dexterity
    elif option == "2":
        os.system('cls')
        heroIG.dexP += 1
        heroIG.points -= 1
        print("You have increased Dexterity!")
        option = input('')
        points()
    #Charisma
    elif option == "3":
        os.system('cls')
        heroIG.chaP += 1
        heroIG.points -= 1
        print("You have increased Charisma!")
        option = input('')
        points()
    #Intelligence
    elif option == "4":
        os.system('cls')
        heroIG.intelP += 1
        heroIG.points -= 1
        print("You have increased Intelligence!")
        option = input('')
        points()
    #Intuition
    elif option == "5":
        os.system('cls')
        heroIG.intuiP += 1
        heroIG.points -= 1
        print("You have increased Intuition!")
        option = input('')
        points()
    #Vitality
    elif option == "6":
        os.system('cls')
        heroIG.vitP += 1
        heroIG.points -= 1
        print("You have increased Vitality")
        option = input('')
        points()
    #Luck
    elif option == "7":
        os.system('cls')
        heroIG.lucP += 1
        heroIG.points -= 1
        print("You have increased Luck")
        option = input('')
        points()
    #Precision
    elif option == "8":
        os.system('cls')
        heroIG.prcP += 1
        heroIG.points -= 1
        print("You have increased Precision")
        option = input('')
        points()
    #Magic **RENAME**
    elif option == "9":
        os.system('cls')
        heroIG.mgcP += 1
        heroIG.points -= 1
        print("You have increased Magic")
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
    print("Luck: %i" % heroIG.lucP)
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
