import os

#Creates the hero class
class hero:
    def __init__(self, name):
        #The name will be inputed by the user
        self.name = name
        #The strength is set by us, however, will be editable throgh points
        self.strength = 10
        #These are the points to edit attributes with
        self.points = 10

def main():
    #Normal print function
    print("Hello, what is your name?")
    #This takes your input and defines it as "option"
    option = input("--> ")
    #heroIG is just Hero In Game. This is needed. Don't know why.
    global heroIG
    #This makes the name of your hero - "option"
    heroIG = hero(option)
    #This directs it to points()
    points()

def points():
    #This clears the terminal
    os.system('cls')
    #This shows the points available
    print("Attribute points available: ", heroIG.points)
    #\n is a break (like an enter)
    print("What would you like to level up:\n1.) Strength")
    option = input('--> ')
    #If you have less than or equal to 0 points:
    if heroIG.points <= 0:
        os.system('cls')
        print("You don't have enough attribute points!")
        #This is just a pause, waiting for the player to press enter
        option = input('')
        #Redirects to the beginning of points
        points()
    #If the input was "1":
    elif option == "1":
        os.system('cls')
        #Hero's strength increases by 1
        heroIG.strength += 1
        #Hero's points decrease by 1
        heroIG.points -= 1
        print("You have increased Strength!")
        option = input('')
        points()
    else:
        points()

#This starts the whole thing
main()
