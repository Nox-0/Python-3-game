import os
import sys
import random
import math

class hero:
    def __init__(self, name):
        self.name = name
        self.lvl = 1
        self.maxhealth = 150
        self.health = self.maxhealth
        self.maxstamina = 20
        self.stamina = self.maxstamina
        self.maxmana = 20
        self.mana = self.maxmana
        self.weak = "matk"
        self.patk = 40
        self.matk = 25
        self.crm = 1.1
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
        self.maxhealth = 20
        self.health = self.maxhealth
        self.maxstamina = 20
        self.stamina = self.maxstamina
        self.maxmana = 20
        self.mana = self.maxmana
        self.crm = 1.5
        self.patk = 20
        self.matk = 10
        self.weak = "patk"
        self.pdef = 1
        self.mdef = 5
goblinKing = GoblinKing("Goblin King")

def setup():
    os.system('cls')
    print("You are about to face the wicked Goblin King.")
    print("What is your name, hero?")
    nameChoice = input("--> ")
    global heroP
    heroP = hero(nameChoice)
    os.system('cls')
    print("Well then, %s, Good luck on your battle." % heroP.name)
    input()
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
    boss.stamina = boss.maxstamina
    boss.mana = boss.maxmana
    heroturn()

def heroturn():
    #Enemy and Hero has seperate turns now, so everything that was related to the enemy is now in its own method.
    os.system('cls')

    print("%s                   vs                 %s" % (heroP.name, boss.name))
    print("Health: %d/%d                          Health: %d/%d" % (heroP.health, heroP.maxhealth, boss.health, boss.maxhealth))
    print("Stamina: %i/%i                           Stamina: %i/%i" % (heroP.stamina, heroP.maxstamina, boss.stamina, boss.maxstamina))
    print("Mana: %i/%i                              Mana: %i/%i" % (heroP.mana, heroP.maxmana, boss.mana, boss.maxmana))
    print("\n1.) Physical Attack")
    print("2.) Magic Attack")
    #new mechanic: defending. Will see a little bit down further. NOT READY YET.
    print("3.) Defend [DOESNT DO ANYTHING ATM]")
    print("\n0.) Run")
    #temp for testing purposes
    print("9.) Exit")
    option = input("--> ")

    if(option == "1"):
        os.system('cls')
        if(heroP.stamina <= 1):
            print("You don't have enough stamina to use a physical attack!")
            heroturn()
        else:
            heroP.stamina -= 2
            heropatk()
    elif(option == "2"):
        os.system('cls')
        if(heroP.mana <= 1):
            print("You don't have enough mana to use a magical attack!")
            heroturn()
        else:
            heroP.mana -= 2
            heromatk()
        heromatk()
    elif(option == "3"):
        os.system('cls')
        herodef()
    elif(option == "0"):
        os.system('cls')
        run()
    elif(option == "9"):
        os.system('cls')
        print("Goodbye.")
        sys.exit()
    else:
        heroturn()

def heropatk():
    heroP.stamina -= 2

    while(heroP.stamina != heroP.maxstamina):
        heroP.stamina += 1
    while(heroP.mana != heroP.maxmana):
        heroP.mana +=1

    crit = random.randint(1, 5)
    hatk = random.randint(math.floor((heroP.patk)/2), (heroP.patk))
    #This version weakness and crit multiplier happens after the initial damage roll.
    if (hatk == math.floor((heroP.patk)/2)):
        print("You missed!")
        input()
        bossturn()

    if(boss.weak == "patk"):
        hatk = math.ceil((hatk*0.2))
        print("It's super effective!")
        input()

    if(crit == 1):
        hatk = math.ceil((hatk+(hatk*heroP.crm)))
        print("Critical Hit!")
        input()

    hatk -= boss.pdef
    #This is incase the hatk is too low
    if (hatk <= 0):
        print("You dealt 0 physical damage!")
        input()
        bossturn()
    else:
        hatk
        boss.health -= hatk
        print("You dealt %s physical damage to the %s" % (str(hatk), boss.name))
        input()

        if(boss.health <= 0):
            victory()
        else:
            bossturn()


def heromatk():
    heroP.mana -= 2

    while(heroP.stamina != heroP.maxstamina):
        heroP.stamina += 1
    while(heroP.mana != heroP.maxmana):
        heroP.mana +=1

    crit = random.randint(1, 5)
    hatk = random.randint(math.floor(heroP.matk/2), (heroP.matk))

    if (hatk == math.floor((heroP.matk)/2)):
        print("You missed!")
        input()
        bossturn()

    if(boss.weak == "matk"):
        hatk = math.ceil((hatk*0.2))
        print("It's super effective!")
        input()

    if(crit == 1):
        hatk = math.ceil((hatk+(hatk*heroP.crm)))
        print("Critical Hit!")
        input()

    hatk -= boss.mdef

    if (hatk <= 0):
        print("You dealt 0 damage!")
        input()
        bossturn()
    else:
        boss.health -= hatk
        print("You dealt %s damage to the %s" % (str(hatk), boss.name))
        input()

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
    os.system('cls')
    #If somehow the boss does not have any stamina or mana remaining.
    if(boss.stamina <=1 and boss.mana <=1):
        print("The boss couldn't do anything!")
        input()
        while(boss.stamina != boss.maxstamina):
            boss.stamina += 1
        while(boss.mana != boss.maxmana):
            boss.mana +=1

        heroturn()

    bossOption = random.randint(1, 2)
    if(bossOption == 1):
        bosspatk()
    elif(bossOption == 2):
        bossmatk()

def bosspatk():
    crit = random.randint(1, 10)
    if(boss.stamina <=4):
        if(boss.stamina <=1):
            bossmatk()
        else:
            boss.stamina -= 2
            batk = random.randint(math.floor((boss.patk)/2), (boss.patk))
            if(crit == 1):
                batk = math.ceil(batk * boss.crm)
                print("Critical Hit!")
                input()

            batk-hero.pdef
            if (batk <= 0):
                print("The boss dealt 0 physical damage!")
                input()
                while(boss.stamina != boss.maxstamina):
                    boss.stamina += 1
                while(boss.mana != boss.maxmana):
                    boss.mana +=1
                heroturn()
            else:
                heroP.health -= batk
                print("The boss dealt %s physical damage to %s!" % (str(batk), heroP.name))
                input()

            if(heroP.health <= 0):
                defeat()
            else:
                while(boss.stamina != boss.maxstamina):
                    boss.stamina += 1
                while(boss.mana != boss.maxmana):
                    boss.mana +=1
                heroturn()
    else:
        #lifesteal ability (ignores armour)
        skillChoice = random.randint(1, 4)
        if(skillChoice == 1):
            boss.mana -= 5
            lifestealatk = random.randint(math.floor((boss.patk)/4), math.floor(boss.patk/2))
            heroP.health -= lifestealatk
            boss.health += lifestealatk
            print("The boss drained %i from your health and gained it as health!" % lifestealatk)
            input()

            if(heroP.health <= 0):
                defeat()

            else:
                while(boss.stamina != boss.maxstamina):
                    boss.stamina += 1
                while(boss.mana != boss.maxmana):
                    boss.mana +=1

                heroturn()

        else:
            boss.stamina -= 2
            batk = random.randint(math.floor((boss.patk)/2), (boss.patk))
            if(crit == 1):
                batk = math.ceil(batk * boss.crm)
                print("Critical Hit!")
                input()

            if ((batk - heroP.pdef) <= 0):
                print("The boss dealt 0 physical damage!")
                input()
                heroturn()

            heroP.health -= batk
            print("The boss dealt %s physical damage to %s." % (str(batk), heroP.name))
            input()

            if(heroP.health <= 0):
                defeat()
            else:
                while(boss.stamina != boss.maxstamina):
                    boss.stamina += 1
                while(boss.mana != boss.maxmana):
                    boss.mana +=1
                heroturn()


def bossmatk():
    crit = random.randint(1, 5)
    if(boss.mana <=4):
        if(boss.mana <=1):
            bossmatk()
        else:
            boss.mana -= 2
            batk = random.randint(math.floor((boss.matk)/2), (boss.matk))
            if(crit == 1):
                batk = math.ceil(batk * boss.crm)
                print("Critical Hit!")
                input()

            if (batk - hero.pdef <= 0):
                print("The boss dealt 0 magic damage!")
                input()
                heroturn()

            heroP.health -= batk
            print("The boss dealt %s magic damage to %s!" % (str(batk), heroP.name))
            input()

            if(heroP.health <= 0):
                defeat()
            else:
                while(boss.stamina != boss.maxstamina):
                    boss.stamina += 1
                while(boss.mana != boss.maxmana):
                    boss.mana +=1
                heroturn()
    else:
        skillChoice = random.randint(1, 2)
        if(skillChoice == 1):
        #attacks multiple times (unable to critical hit)
            boss.mana -= 5
            amtshots = random.randint(1, 5)
            if(amtshots == 1):
                batk = random.randint(math.floor((boss.matk)/2), (boss.matk))
                batk -= heroP.mdef
                heroP.health -= batk
                print("%s fired bolts at you %i times and dealt %i damage!" % (boss.name, amtshots, batk))
                input()
            elif(amtshots == 2):
                batk = random.randint(math.floor((boss.matk)/2), (boss.matk))
                batk = batk * 2
                batk -= heroP.mdef
                heroP.health -= batk
                print("%s fired bolts at you %i times and dealt %i damage!" % (boss.name, amtshots, batk))
                input()

            elif(amtshots == 3):
                batk = random.randint(math.floor((boss.matk)/2), (boss.matk))
                batk = batk * 3
                batk -= heroP.mdef
                heroP.health -= batk
                print("%s fired bolts at you %i times and dealt %i damage!" % (boss.name, amtshots, batk))
                input()

            elif(amtshots == 4):
                batk = random.randint(math.floor((boss.matk)/2), (boss.matk))
                batk = batk * 4
                batk -= heroP.mdef
                heroP.health -= batk
                print("%s fired bolts at you %i times and dealt %i damage!" % (boss.name, amtshots, batk))
                input()

            else:
                batk = random.randint(math.floor((boss.matk)/2), (boss.matk))
                batk = batk * 5
                batk -= heroP.mdef
                heroP.health -= batk
                print("%s fired bolts at you %i times and dealt %i damage!" % (boss.name, amtshots, batk))
                input()


            if(heroP.health <= 0):
                    defeat()

            else:
                while(boss.stamina != boss.maxstamina):
                        boss.stamina += 1
                while(boss.mana != boss.maxmana):
                        boss.mana +=1

                heroturn()

        else:
            boss.mana -= 2
            batk = random.randint(math.floor((boss.matk)/2), (boss.matk))
            if(crit == 1):
                batk = math.ceil(batk * boss.crm)
                print("Critical Hit!")
                input()

            batk -= heroP.mdef

            if (batk <= 0):
                print("The boss dealt 0 physical damage!")
                input()
                heroturn()

            heroP.health -= batk
            print("The boss dealt %s physical damage to %s" % (str(batk), heroP.name))
            input()

            if(heroP.health <= 0):
                defeat()
            else:
                while(boss.stamina != boss.maxstamina):
                    boss.stamina += 1
                while(boss.mana != boss.maxmana):
                    boss.mana +=1
                heroturn()


def victory():
    os.system('cls')
    print("Well done! You have defeated the %s!" % boss.name)
    print("Now do it again.")
    option = input()
    prefight()

def defeat():
    os.system('cls')
    print("You lost! You failed to defeat the %s which had %i health remaining!" % (boss.name, boss.health))
    input()
    print("You will now try again.")
    option = input()
    prefight()

def run():
    if boss.stamina <= 0:
        os.system('cls')
        print("You have successfully ran away!")
        print("But I mean what's the fun in that?")
        print("Fight again!")
        prefight()
    else:
        os.system('cls')
        print("You cannot run from a boss fight unless the boss is out of stamina!")
        print("Because of your attempt, the enemy has gotten an upper hand in the fight!")
        input()
        bossturn()

setup()
