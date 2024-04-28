import random

random_no: int = random.randint(0, 10)
guesses: int = 3

while guesses != 0:
    print(f"Number of guesses remaining: {guesses}")
    try:
        n : int = int(input("Guess a number between 1 to 10 : "))
    except ValueError as e:
        print("Please enter a valid number!")
        continue

    if guesses <= 1:
        print("You ran out of guesses, you lose!!!")
        break

    if n == random_no:
        print("You guessed right!")
        break
    elif n < random_no:
        guesses -= 1
        print("The number is higher!")
    else: 
        guesses -= 1
        print("The number is lower!")

