import random
compScore = 0
playerScore = 0
rounds = 5

while rounds > 0:
    compChoices = ["Rock", "Paper", "Scissors"]

    compPicked = random.choice(compChoices)

    userChoice = input("(a) Rock\n(b) Paper\n(c) Scissors\n")

    if userChoice == "a" and compPicked == "Rock":
        print("Your rock bumps off the computer's rock. Draw!")
        rounds -= 1
        print("Score: " + str(playerScore))
        print("Rounds left: " + str(rounds))
    elif userChoice == "a" and compPicked == "Paper":
        print("Your rock is covered by the computer's paper. You lose!")
        rounds -= 1
        compScore += 1
        print("Score: " + str(playerScore))
        print("Rounds left: " + str(rounds))
    elif userChoice == "a" and compPicked == "Scissors":
        print("Your rock crushes the computer's scissors. You win!")
        rounds -= 1
        playerScore += 1
        print("Score: " + str(playerScore))
        print("Rounds left: " + str(rounds))
    elif userChoice == "b" and compPicked == "Rock":
        print("Your paper covers the computer's rock. You win!")
        rounds -= 1
        playerScore +1
        print("Score: " + str(playerScore))
        print("Rounds left: " + str(rounds))
    elif userChoice == "b" and compPicked == "Paper":
        print("Your paper collides with the computer's paper. Draw!")
        rounds -= 1
        print("Score: " + str(playerScore))
        print("Rounds left: " + str(rounds))
    elif userChoice == "b" and compPicked == "Scissors":
        print("Your paper is cut in half by the computer's scissors. You lose!")
        rounds -= 1
        compScore += 1
        print("Score: " + str(playerScore))
        print("Rounds left: " + str(rounds))
    elif userChoice == "c" and compPicked == "Rock":
        print("Your scissors are crushed by the computer's rock. You lose!")
        rounds -= 1
        compScore += 1
        print("Score: " + str(playerScore))
        print("Rounds left: " + str(rounds))
    elif userChoice == "c" and compPicked == "Paper":
        print("Your scissors cut the computer's paper in half. You Win!")
        rounds -= 1
        playerScore += 1
        print("Score: " + str(playerScore))
        print("Rounds left: " + str(rounds))
    elif userChoice == "c" and  compPicked == "Scissors":
        print("Your scissors rub against the computer's scissors. Draw!")
        rounds -= 1
        print("Score: " + str(playerScore))
        print("Rounds left: " + str(rounds))
    else:
        print("Invalid input.")

print("-------------")

if playerScore > compScore:
    print("You won the game!")
    print("Your score: " + str(playerScore))
    print("Computer score: " + str(compScore))
elif playerScore < compScore:
    print("You lost the game!")
    print("Your score: " + str(playerScore))
    print("Computer score: " + str(compScore))
else:
    print("Draw!")
    print("Your score: " + str(playerScore))
    print("Computer score: " + str(compScore))