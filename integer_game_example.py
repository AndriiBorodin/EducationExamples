import random
print("Integer Game")
score = 0
for x in range(5):
    A = random.randint(-10, 10)
    B = random.randint(-10, 10)
    print(A, "and", B)
    operation = input("Add or subtract? ")
    operation = operation.lower()
    if operation == "add":
        print(A, "+", B, "=", A+B)
        score = score + A + B
    else:
        print(A, "-", B, "=", A-B)
        score = score + A - B
    print("Your score is now", score)
    print("You have", 4-x, "turns remaining")
input("Press ENTER to exit.")