import random
from sympy import Symbol, Eq, solve, pretty_print

def generate_equations():
    x = Symbol('x')
    y = Symbol('y')

    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    d = random.randint(-10, 10)

    one_step_eq = a*x + b
    two_step_eq = c*y + d

    eq_1 = Eq(one_step_eq, 0)
    eq_2 = Eq(two_step_eq, 0)

    return eq_1, eq_2

def main():
    while True:
        eq_1, eq_2 = generate_equations()

        print("One step equation is:")
        pretty_print(eq_1)
        print("\nTwo step equation is:")
        pretty_print(eq_2)
        print()

        while True:
            guess = input("Guess the solutions of these problems, write in the form x,y: ")
            try:
                x_guess, y_guess = map(float, guess.split(","))
            except ValueError:
                print("Please enter two numbers separated by a comma.")
                continue

            solution_x = round(float(solve(eq_1)[0]), 1)
            solution_y = round(float(solve(eq_2)[0]), 1)

            print(f"The actual answers are x: {solution_x} and y: {solution_y}")

            if x_guess == solution_x and y_guess == solution_y:
                print("You are right!!")
                break
            else:
                print("You are wrong. Let's try another problem.")
                break  # Exit the current loop to generate new equations

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
