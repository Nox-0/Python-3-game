import os
import sys
import random
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
        self.patk = 10
        self.matk = 10
        #Crit multiplier
        self.crm = 5
        self.pdef = 1
        self.mdef = 1
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

#Created a class named goblin
class goblin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        #This is the max attack
        self.attack = 5
        #This is what the enemy is weak against
        self.weak = "patk"
#This is the name
goblinIG = goblin("Goblin")

#Created a class named zombie
class zombie:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        #This is the max attack
        self.attack = 7
        #This is what the enemy is weak against
        self.weak = "matk"
#This is the name
zombieIG = zombie("Zombie")

#Created a class name bgoblin (This is a boss)
class bgoblin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        #This is the max attack
        self.attack = 20
        #This is what the enemy is weak against
        self.weak = "patk"
#This is the name
bgoblinIG = bgoblin("Goblin Boss")

#Created a class named bzombie (This is a boss)
class bzombie:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 140
        self.health = self.maxhealth
        #This is the max attack
        self.attack = 28
        #This is what the enemy is weak against
        self.weak = "matk"
#This is the name
bzombieIG = bzombie("Zombie Boss")


def main():
    os.system('cls')
    print("Hello, what is your name?")
    option = input("--> ")
    #Makes heroIG able to be used anywhere
    global heroIG
    heroIG = hero(option)
    prefight()


def prefight():
    #enemy becomes global
    global enemy
    #This decides your enemy
    enemynum = random.randint(1, 2)
    if enemynum == 1:
        #1 in 10 chance to fight boss
        bnum = random.randint (1, 10)
        if bnum == 1:
            enemy = bgoblinIG
        else:
            enemy = goblinIG
    elif enemynum == 2:
        #Same as above
        bnum = random.randint (1, 10)
        if bnum == 1:
            enemy = bzombieIG
        else:
            enemy = zombieIG
    else:
        #Takes you back to the start if it fails (which it shouldn't...)
        prefight()
    heroIG.health = heroIG.maxhealth
    heroIG.stamina = heroIG.maxstamina
    heroIG.mana = heroIG.maxmana
    enemy.health = enemy.maxhealth
    fight()


def fight():
    os.system('cls')
    global hatk
    global eatk
    #1 in 2 chance fo getting a crit (for testing purposes)
    crit = random.randint(1,2)
    #The enemy's attack will equal equal a random integer between 1/2 of the attack and their attack
    eatk = random.randint(math.floor(enemy.attack/2), (enemy.attack))
    print("%s              vs            %s" % (heroIG.name, enemy.name))
    print("%s\'s Health: %d/%d          %s\'s Health: %d/%d" % (heroIG.name, heroIG.health, heroIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth))
    print("Stamina: %i" % heroIG.stamina)
    print("Mana: %i" % heroIG.mana)
    print("1.) Physical Attack\n2.) Magic Attack\n0.) Run")
    option = input("--> ")
    if option == "1":
        heroIG.stamina -= 1
        if crit == 1:
            #The hero's attack will equal equal a random integer between 1/2 of the attack and their attack multiplied by the crit multiplier
            hatk = random.randint(math.floor(heroIG.patk/2), (heroIG.patk * heroIG.crm))
            os.system('cls')
            print("CRIT!")
            input()
        else:
            #The hero's attack will equal equal a random integer between 1/2 of the attack and their attack
            hatk = random.randint(math.floor(heroIG.patk/2), (heroIG.patk))
        pattack()
    elif option == "2":
        heroIG.mana -= 1
        if crit == 1:
            #The hero's attack will equal equal a random integer between 1/2 of the attack and their attack multiplied by the crit multiplier
            hatk = random.randint(math.floor(heroIG.matk/2), (heroIG.matk * heroIG.crm))
            os.system('cls')
            print("CRIT!")
            input()
        else:
            #The hero's attack will equal equal a random integer between 1/2 of the attack and their attack
            hatk = random.randint(math.floor(heroIG.matk/2), (heroIG.matk))
        mattack()
    elif option == "0":
        run()
    else:
        fight()


def pattack():
    os.system('cls')
    #If the enemy's weakness is a physical attack
    if enemy.weak == "patk":
        #The hero's attack multiplies itself by the modifier
        #The enemy's health decreases by the hero's final attack
        enemy.health -= (hatk * 2)
        print("It's super effective!\nYou deal %i damage!" % (hatk * 2))
    #If the attack is half of the hero's attack, you miss
    elif hatk == heroIG.patk/2:
        print("You miss!")
    #For all other attacks, it's just that:
    else:
        enemy.health -= hatk
        print("You deal %i damage!" % hatk)
    option = input()
    #If the enemy's attack reaches 0, it takes you to win()
    if enemy.health <= 0:
        win()
    os.system('cls')
    #Enemy attack misses
    if eatk == enemy.attack/2:
        print("The %s missed!" % enemy.name)
    #All other attacks
    else:
        heroIG.health -= eatk
        print("The %s deals %i damage!" % (enemy.name, eatk))
    option = input()
    #If the hero's attack reaches 0, it takes you to dead()
    if heroIG.health <= 0:
        dead()
    #Then it takes you to fight()
    else:
        fight()


def mattack():
    os.system('cls')
    if enemy.weak == "matk":
        enemy.health -= (hatk * 2)
        print("It's super effective!\nYou deal %i damage!" % (hatk * 2))
    elif hatk == heroIG.matk/2:
        print("You miss!")
    else:
        enemy.health -= hatk
        print("You deal %i damage!" % hatk)
    option = input()
    if enemy.health <= 0:
        win()
    os.system('cls')
    if eatk == enemy.attack/2:
        print("The %s missed!" % enemy.name)
    else:
        heroIG.health -= eatk
        print("The %s deals %i damage!" % (enemy.name, eatk))
    option = input()
    if heroIG.health <= 0:
        dead()
    else:
        fight()


def run():
    os.system('cls')
    #You have a 1 in 2 chance of running away (for testing purposes)
    runnum = random.randint(1,2)
    if runnum == 1:
        print("You technically ran away, but since there's nowhere to run to, you just restart the fight.")
        option = input()
        prefight()
    else:
        print("You failed to get away!")
        option = input()
        os.system('cls')
        if eatk == enemy.attack/2:
            print("The %s missed!" % enemy.name)
        else:
            heroIG.health -= eatk
            print("The %s deals %i damage!" % (enemy.name, eatk))
        option = input()
        if heroIG.health <= 0:
            dead()
        else:
            fight()


def win():
    os.system('cls')
    print("Well done! You have defeated the %s!" % enemy.name)
    print("Now do it again.")
    option = input()
    prefight()


def dead():
    os.system('cls')
    print("You are dead.")
    print("Restart!")
    option = input()
    main()




main()
