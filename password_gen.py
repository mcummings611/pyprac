import random

chars = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()")

runAgain = True

while runAgain:
    password_len = int(input("What length would you like your password to be: "))
    password_count =  int(input("How many passwords do you want to generate: "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here is your password: " + password)