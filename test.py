while True:
    try:
        user_input = input("Enter the name of the nodes to connect (example: 0 1): ")
        a = int(user_input.split(" ")[0])
        b = int(user_input.split(" ")[1])

        if a < 0 or a > 5 or b < 0 or b > 5:
            raise ValueError
    except:
        print("Sorry, the entered input is not valid. Try again.")
        continue
    else:
        print("yaay. that works")
        break


