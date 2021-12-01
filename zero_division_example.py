
while True:
    try:
        x = int(input())
        result = 10 / x
    except ZeroDivisionError:
        print("Zero division Fail")
        exit(0)
    except ValueError:
        print("Type not integer")
        exit(0)
    else:
        print("Pass case")
        print(result)
        exit(1)

