def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ").strip()
    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice")
        return

    try:
        a = float(input("Enter first number: ").strip())
        b = float(input("Enter second number: ").strip())
    except ValueError:
        print("Please enter valid numbers.")
        return

    try:
        if choice == "1":
            result = add(a, b)
            symbol = "+"
        elif choice == "2":
            result = subtract(a, b)
            symbol = "-"
        elif choice == "3":
            result = multiply(a, b)
            symbol = "*"
        else:
            result = divide(a, b)
            symbol = "/"

        print(f"{a} {symbol} {b} = {result}")
    except ValueError as err:
        print(err)


if __name__ == "__main__":
    main()
