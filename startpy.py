import sys
import os
import pickle
import Player
import Items



def start():
    os.system('cls')
    print("Hello, what is your name?")
    nameChoice = input("--> ")
    global heroP
    heroP = Player.hero(nameChoice)
    start0()

def start0():
    os.system('cls')
    print("Welcome, %s!" % heroP.name)
    option = input('')
    start1()

def start1():
    os.system('cls')
    print("Stats:\n")
    print("Name: %s" % heroP.name)
    print("Physical Attack: %i" % heroP.patk)
    print("Magic Attack: %i" % heroP.matk)
    print("Health: %i/%i" % (heroP.health, heroP.maxhealth))
    print("Stamina: %i/%i" % (heroP.stamina, heroP.maxstamina))
    input()
    import menu1py
    menu1py.menu1()
