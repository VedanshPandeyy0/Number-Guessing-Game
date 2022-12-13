import random

random_number = random.randint(1, 100)
guesses = 0

while True:
    guesses += 1
    user_guess = int(input("Guess a number between 1 to 100: "))

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print(f"You got it in {guesses} guesses!")