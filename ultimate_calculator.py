import math
import sympy
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve

def add():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print("The sum is ", a + b)

def subtract():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print("The difference is ", a - b)

def multiply():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print("The product is ", a * b)

def divide():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    print("The quotient is ", a / b)

def is_prime():
    n = int(input("Enter a number: "))
    if n <= 1:
        print("Not prime")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("Not prime")
                break
        else:
            print("Prime")

def prime_factors():
    n = int(input("Enter a number: "))
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    print("Prime factors:", factors)

def simplify_sqrt():
    n = float(input("Enter a number: "))
    if n < 0:
        print("Cannot simplify the square root of a negative number")
    else:
        upper_limit = math.floor(math.sqrt(n)) + 1
        max_factor = 1
        other_factor = 1
        square_root = 1

        for maybe_factor in range(1, upper_limit):
            if n % (maybe_factor ** 2) == 0:
                max_factor = maybe_factor

        other_factor = n / max_factor

        square_root = int(math.sqrt(max_factor))
        other_factor = int(other_factor)
        output = square_root * sympy.sqrt(other_factor)
        print("Simplified square root:", output)

def solve_equation():
    x = symbols('x')

    eq = input('Enter an equation to solve for x: 0 = ')

    solved_eq = solve(eq, x)
    if solved_eq:
        print("x =", solved_eq[0])
    else:
        print("No solution found for the given equation.")

def plot_equation(equation_str=None):
    if not equation_str:
        equation_str = input('Enter an equation in terms of x: ')
    x = symbols('x')

    try:
        # Check for simple equations (constant multiplied by x)
        if equation_str.strip() == f"{sympy.Symbol('C')}*x":  # Replace "C" with any character representing a constant
            solution = solve(equation_str, x)[0]
            print(f"The solution to the equation is: x = {solution}")
            return  # Don't attempt plotting for simple equations

        # Parse the equation using sympy
        equation = sympy.sympify(equation_str)

        # Generate x and y values
        x_values = np.linspace(-10, 10, 400)
        y_values = sympy.lambdify(x, equation)(x_values)

        # Plot the graph
        plt.figure(figsize=(8, 6))
        plt.plot(x_values, y_values, label=equation_str)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graph of ' + equation_str)
        plt.grid(True)
        plt.legend()
        plt.show()
    except:
        print("Invalid equation format. Please enter a valid expression in terms of x.")

print("Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Check if a number is prime")
print("6. Find prime factors of a number")
print("7. Simplify a square root")
print("8. Solve an equation")
print("9. Plot an equation")
print("10. Exit")

choice = int(input("Enter your choice: "))

while choice != 10:
    if choice == 1:
        add()
    elif choice == 2:
        subtract()
    elif choice == 3:
        multiply()
    elif choice == 4:
        divide()
    elif choice == 5:
        is_prime()
    elif choice == 6:
        prime_factors()
    elif choice == 7:
        simplify_sqrt()
    elif choice == 8:
        solve_equation()
    elif choice == 9:
        plot_equation()
    else:
        print("Invalid choice")

    choice = int(input("Enter your choice: "))

print("Exiting...")
