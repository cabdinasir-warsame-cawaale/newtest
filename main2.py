def calculator():
    print("Welcome to the Python Calculator!")
    print("Select an operation to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        try:
            choice = input("Enter choice (1/2/3/4): ")
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is undefined.")
                else:
                    print(f"{num1} / {num2} = {num1 / num2}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if next_calculation != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter numerical values.")

# Run the calculator
calculator()
