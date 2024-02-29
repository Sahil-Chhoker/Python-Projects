import matplotlib.pyplot as plt
import numpy as np
import random

xmin = -10
xmax = 10
ymin = -10
ymax = 10

def plot_point():
    x = random.randint(xmin, xmax)
    y = random.randint(ymin, ymax)

    fig, ax = plt.subplots()
    plt.axis([xmin, xmax, ymin, ymax])
    plt.plot([xmin, xmax], [0, 0], 'b')
    plt.plot([0, 0], [ymin, ymax], 'b')
    plt.grid()

    plt.plot([x], [y], 'ro')
    plt.show()

    return x, y

def main():
    while True:
        x, y = plot_point()

        while True:
            guess = input("Guess the x and y with a comma (or 'q' to quit): ")

            if guess.lower() == 'q':
                print("Thanks for playing!")
                return

            try:
                x_guess, y_guess = map(float, guess.split(","))
                break
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a comma.")

        print(f"The real x and y are: {x}, {y}")

        if x == x_guess and y == y_guess:
            print("You got it right!!!")
        else:
            print("You failed! Try again.")

if __name__ == "__main__":
    main()
