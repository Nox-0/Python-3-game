import os
import sys
import random
import time
import math

class hero:
    def __init__(self, name):
        self.name = name
        self.lvl = 1
        self.maxhealth = 100
        self.health = self.maxhealth
        self.maxstamina = 20
        self.stamina = self.maxstamina
        self.maxmana = 20
        self.mana = self.maxmana
        self.weak = "matk"
        self.patk = 1.1
        self.matk = 10
        self.crm = 2
        self.pdef = 10
        self.mdef = 5
        self.strP = 0
        self.dexP = 0
        self.chaP = 0
        self.intelP = 0
        self.intuiP = 0
        self.vitP = 0
        self.lukP = 0
        self.prcP = 0
        self.mgcP = 0
        self.points = 20

class GoblinKing:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 250
        self.health = self.maxhealth
        self.maxstamina = 20
        self.stamina = self.maxstamina
        self.maxmana = 20
        self.mana = self.maxmana
        self.patk = 20
        self.matk = 10
        self.weak = "patk"
        self.pdef = 5
        self.mdef = 5
goblinKing = GoblinKing("Goblin King")

def setup():
    os.system('cls')
    print("You are about to face the wicked Goblin King.")
    #console will pause for 2 seconds.
    time.sleep(2)
    print("What is your name, hero?")
    nameChoice = input("--> ")
    global heroP
    heroP = hero(nameChoice)
    os.system('cls')
    print("Well then, %s, Good luck on your battle." % heroP.name)
    time.sleep(2)
    prefight()

def prefight():
    global boss
    #To determine what boss the player will be versing.
    #Currently it's only going to pick goblinKing.
    bossChoice = random.randint(1,2)
    if(bossChoice == 1):
        boss = goblinKing
    else:
        boss = goblinKing

    heroP.health = heroP.maxhealth
    heroP.stamina = heroP.maxstamina
    heroP.mana = heroP.maxmana
    boss.health = boss.maxhealth
    heroturn()

def heroturn():
    #Enemy and Hero has seperate turns now, so everything that was related to the enemy is now in its own method.
    os.system('cls')

    print("%s                     vs            %s" % (heroP.name, boss.name))
    print("%s\'s Health: %d/%d                 %s\'s Health: %d/%d" % (heroP.name, heroP.health, heroP.maxhealth, boss.name, boss.health, boss.maxhealth))
    print("Stamina: %i/%i                           Stamina: %i/%i" % (heroP.stamina, heroP.maxstamina, boss.stamina, boss.maxstamina))
    print("Mana: %i/%i                              Mana: %i/%i" % (heroP.mana, heroP.maxmana, boss.mana, boss.maxmana))
    print("\n1.) Physical Attack")
    print("2.) Magic Attack")
    #new mechanic: defending. Will see a little bit down further. NOT READY YET.
    print("3.) Defend")

    print("\n0.) Run")
    #temp for testing purposes
    print("9.) Exit")
    option = input("--> ")

    if(option == "1"):
        os.system('cls')
        heropatk()
    elif(option == "2"):
        os.system('cls')
        heromatk()
    elif(option == "3"):
        os.system('cls')
        herodef()
    elif(option == "4"):
        os.system('cls')
        run()
    elif(option == "9"):
        os.system('cls')
        print("Goodbye.")
        sys.exit()
    else:
        pass

def heropatk():
    heroP.stamina -= 2
    crit = random.randint(1, 5)
    hatk = random.randint(math.floor(heroP.patk/2), (heroP.patk))
    #This version weakness and crit multiplier happens after the initial damage roll.
    if(boss.weak == "patk"):
        hatk *= 0.2

    if(crit == 1):
        hatk = hatk * heroP.crm
        print("Critical Hit!")
        time.sleep(1)
    #This is incase the hatk is too low
    if (hatk - boss.pdef <= 0):
        print("You dealt 0 damage!")
        bossturn()

    boss.health -= hatk
    print("You dealt %s damage to the %s" % (str(patk), boss.name))

    if(boss.health <= 0):
        victory()
    else:
        while(heroP.stamina != heroP.maxstamina):
            heroP.stamina += 1
        bossturn()


def heromatk():
    crit = random.randint(1, 5)
    hatk = random.randint(math.floor(heroP.matk/2), (heroP.matk))
    if(boss.weak == "patk"):
        hatk *= 0.2
        print("It's super effective!")
        time.sleep(1)

    if(crit == 1):
        hatk = hatk * heroP.crm
        print("Critical Hit!")
        time.sleep(1)

    if (hatk - boss.mdef <= 0):
        print("You dealt 0 damage!")
        bossturn()

    boss.health -= hatk
    print("You dealt %s damage to the %s" % (str(hatk), boss.name))

    if(boss.health <= 0):
        victory()
    else:
        bossturn()

def herodef():
    heroturn()

def bossturn():
    #Moveset: patk, matk, lifesteal(patk), magic bolts(matk)
    #lifesteal will steal x% of current health
    #Magic bolts will deal x amount of damage x times.
    bossOption = random.randint(1, 2)
    if(bossOption == 1):
        os.sys('cls')




def victory():
    os.system('cls')
    print("Well done! You have defeated the %s!" % boss.name)
    print("Now do it again.")
    option = input()
    prefight()

def run():
    print("You tried to run during a boss fight, but it failed!")
    print("Because of your attempt, the enemy has gotten an upper hand in the fight!")
    time.sleep(2)
    bossturn()

setup()
