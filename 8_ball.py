import random

outcomes = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outloook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Very doubtful."
]

playagain = True

while playagain == True:
    randoutcome = random.choice(outcomes)
    question = input("What question do you have for me? ")
    print("------------------")
    print(randoutcome)
    print("------------------")
    playquestion = input("Would you like to play again? Y/N: ").upper()
    if playquestion == "Y":
        playagain = True
    elif playquestion == "N":
        playagain = False
        print("Thanks for playing!")
    else:
        print("Invalid input.")