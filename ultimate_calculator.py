import math
import sympy
from sympy import symbols , solve

def add():
  a = float(input("Enter a number: "))
  b = float(input("Enter another number: "))
  print("The sum is ", a+b)

def subtract():
  a = float(input("Enter a number: "))
  b = float(input("Enter another number: "))
  print("The difference is ", a-b)

def multiply():
  a = float(input("Enter a number: "))
  b = float(input("Enter another number: "))
  print("The product is ", a*b)

def divide():
  a = float(input("Enter a number: "))
  b = float(input("Enter another number: "))
  print("The quotient is ", a/b)

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
        if n % (maybe_factor**2) == 0:
            max_factor = maybe_factor

    other_factor = n/max_factor

    square_root = int(math.sqrt(max_factor))
    other_factor = int(other_factor)
    output = square_root*sympy.sqrt(other_factor)
    print("Simplified square root:", output)

def solve_equation():
    x = symbols('x')

    eq = input('Enter an equation to solve for x: 0 = ')

    solved_eq = solve(eq, x)
    if solved_eq:
        print("x =", solved_eq[0])
    else:
        print("No solution found for the given equation.")

print("Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Check if a number is prime")
print("6. Find prime factors of a number")
print("7. Simplify a square root")
print("8. Solve an equation")
print("9. Exit")

choice = int(input("Enter your choice: "))

while choice != 9:
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
  else:
    print("Invalid choice")

  choice = int(input("Enter your choice: "))

print("Exiting...")
