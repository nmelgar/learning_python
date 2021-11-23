#Write a Python program to guess a number between 1 to 9
import random

print("Welcome to guess the number game!")
while (True):
    users_number = int(input("Choose a number between 1 and 9:  "))
    print("You chose: " + str(users_number))

    computers_number = random.randint(1 ,9)
    print("Computer chose: " + str(computers_number))

    if (users_number == computers_number):
        print("\nCongratulations, you guessed the number!!")
        break
    else:
        print("\nTry again!")
