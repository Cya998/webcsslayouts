def calculator():
    while True:  
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            operation = input("Enter operation (+, -, *, /): ")

            if operation == "+":
                print("Result:", x + y)

            elif operation == "-":
                if x < y:
                    print("❌Error: Cannot subtract a bigger head from a smaller one😔 Try again.\n")
                    continue
                else:
                    print("Result:", x - y)

            elif operation == "*":
                print("Result:", x * y)

            elif operation == "/":
                if y == 0:
                    print("❌Error: Cannot divide by zero! Try again.\n")
                    continue
                else:
                    print("Result:",x / y)

            else:
                print(" Invalid operation babes😭! Use +, -, *, or /.\n")
                continue

            break

        except ValueError:
            print("That’s not a number🤦‍♀️Please enter valid numbers.\n")

    play_again = input("Do you want to calculate again?\n): ").lower()
    if play_again == "yes":
        print("\n New Calculation \n")
        calculator()  
    else:
        print("Thanks for using the calculator!🤞")

calculator()


        

