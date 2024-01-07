import random

i = 0
def choose_sign():
    return random.randint(1, 3)

def check_win(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 0
    elif (
        (player_choice == 1 and computer_choice == 2) or
        (player_choice == 2 and computer_choice == 3) or
        (player_choice == 3 and computer_choice == 1)
    ):
        return 1
    else:
        return -1

def sayResult(result):
    if(result == 0):
        print("Its a Tie!\n\n")
    elif(result == 1):
        print("You Win!!\n\n")
    elif(result == -1):
        print("You Lose\n\n")

while(True):

    print("1: Snake\n2: Water\n3: Gun")
    player_choice = int(input("Write your choice: "))

    computer_choice = choose_sign()

    print(f"The computer chooses: {computer_choice}")

    result = check_win(player_choice, computer_choice)
    sayResult(result)
    i += 1

    if(result > 0):
        break

print(f"It took you {i} attempts to win.\n\n")