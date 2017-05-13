import os
import sys

class Enemy:
    def __init__(self, name, maxhealth, health, atk, weak):
        self.name = name
        self.maxhealth = maxhealth
        self.health = self.maxhealth
        self.atk = atk
        self.weak = weak

class GreenSlime(Enemy):
    def __init__(self):
        super().__init__(name="Green Slime", maxhealth=10, health=self.maxhealth, atk=5, weak="patk")

class GoblinGuard(Enemy):
    def __init__(self):
        super().__init__(name="Goblin Guard", maxhealth=20, health=self.maxhealth, atk=5, weak="patk")
