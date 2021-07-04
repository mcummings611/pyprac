import random
total = 0
stay = False
str1 = """You have {}.
Type 1 to Hit.
Type 2 to Stay.
Remember to get as close to 21 without going over."""
print(str1.format(total))

while total <= 21 and stay == False:
    userinp = input("Enter 1 or 2: ")
    if userinp == "1":
        randnum = random.randrange(1, 12)
        total = total + randnum
        totalStr = "You have {}."
        print(totalStr.format(total))
    elif userinp == "2":
        stay = True
    else:
        print("Invalid entry.")
    
if stay == True:
    stayStr = "You have stayed at {}."
    print(stayStr.format(total))
else:
    bustStr = "You have busted with a total of {}."
    print(bustStr.format(total))

def pc_guess():
    import random
    pctotal = 0
    stay = False
    while pctotal <= 21 and not(stay):
        if pctotal < 16:
            randnum = random.randrange(1,12)
            pctotal += randnum
        elif pctotal >= 16:
            stay = True
    return pctotal

pc_number = pc_guess()
playerBusted = False
if total > 21:
    playerBusted = True

pcBusted = False
if pc_number > 21:
    pcBusted = True

if total < pc_number and not(pcBusted):
    pcWinStr = "You scored {}. The house scored {}. You lost."
    print(pcWinStr.format(total, pc_number))
elif total > pc_number and not(playerBusted):
    playerWinStr = "You scored {}. The house scored {}. You win!"
    print(playerWinStr.format(total, pc_number))
elif pcBusted and playerBusted:
    print("You and the house busted. Draw!")
elif total == pc_number:
    nonBustedDraw = "You and the house scored {}. Draw!"
    print(nonBustedDraw.format(total))