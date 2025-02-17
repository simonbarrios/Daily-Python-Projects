import random

target_number = random.randint(1, 10)
guess = input("Guess a number between 1 and 10: ")

if guess == target_number:
    print("Congratulations!You guessed the number!")
else:
    print("Sorry, the targetnumber was", target_number)




