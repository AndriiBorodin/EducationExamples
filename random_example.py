import random
print("Guess the Number")
number = random.randint(-10, 10)
guess = 100
print("I am thinking of a number")
print("between -10 and 10.")
while (guess != number):
    guess = input("What's the number? ")
    guess = int(guess)
    if (guess > number):
        print("Too high.")
    if (guess < number):
        print("Too low.")
print("Correct!  The number was", number)
input("Press ENTER to exit.")
