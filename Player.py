import os
import sys

class hero:
    def __init__(self, name):
        self.name = name
        self.lvl = 1
        self.maxhealth = 250
        self.health = self.maxhealth
        self.maxstamina = 20
        self.stamina = self.maxstamina
        self.maxmana = 10
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
