""" x = 500

while x > 0:
    x = x - 100
    print(x) """

""" while True:
    z = input("multiply?")
    if z == "exit":
        break """

""" while True:
    z = input("Enter a number to multiply by 2 (or 'exit' to quit): ")
    if z == "exit":
        break
    number = float(z)
    print(number * 2) """


import random
n = random.randint(1, 100)
guess = 1
while True:
    z = int(input("Guess the number (or exit the game):"))
    if z == "exit":
        print("The number was", n)
        break
    elif z > n:
        print("lower")
        guess = guess + 1
    elif z < n:
        print("higher")
        guess = guess + 1
    elif z == n:
        print("CORRECT! It took you", str(guess), "attempt")
        break
    if guess == 10:
        print("You ran out of attempts, the number was", n)
        break
