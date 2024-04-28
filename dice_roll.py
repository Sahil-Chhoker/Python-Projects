import random

def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for _ in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls

def main():
    while True:
        try:
            user_input: str = input("How many dice you want to roll?(press 'q' to quit) ")
            if user_input.lower() == 'q':
                print("Thanks for playing!")
                break

            print(*roll_dice(int(user_input)), sep=', ')
        except ValueError:
            print("Please enter an valid integer!")
            continue

if __name__ == "__main__":
    main()
