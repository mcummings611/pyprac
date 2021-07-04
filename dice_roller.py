import random

def roll_dice():
    die = int(input("What sided dice would you like to roll? "))
    rollCount = int(input("How many times do you want to roll? "))
    for x in range(0, rollCount):
        print("----------------")
        roll = str(random.randrange(1, die + 1))
        print("You have rolled a " + roll + ".")
        print("----------------")

roll_dice()
