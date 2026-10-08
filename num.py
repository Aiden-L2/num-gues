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
guess = 0
history = []
while True:
    z = int(input("Guess the number 1-100(or exit the game):"))
    history.append(z)
    if int(z) == "exit":
        print("The number was", n)
        break
    elif int(z) > n:
        print("lower")
        guess = guess + 1
        print(history)
    elif int(z) < n:
        print("higher")
        guess = guess + 1
        print(history)
    elif int(z) == n:
        guess = guess + 1
        print("CORRECT! It took you", str(guess), "attempt")
        print("num history:", history)
        break
    if guess == 10:
        print("You ran out of attempts, the number was", n)
        print("num history:", history)
        break
