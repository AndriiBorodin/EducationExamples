import sys

user_card_number = input("Enter card number:")
cards_list = ["5115 2344 6023 0880", "5115 4456 0733 1132", "5115 4343 0809 6532"]

for cards in cards_list:
    if user_card_number in cards_list:
        pass
    else:
        sys.exit("Invalid card")


def pin_validator():
    pin = 1111
    counter = 3
    while True:
        a = int(input("Enter pin:"))
        if a == pin:
            print("Welcome to main menu!")
            break
        elif a != pin and counter > 1:
            print("Invalid pin, try again")
            counter -= 1
        else:
            print("Your card blocked")
            break


pin_validator()
