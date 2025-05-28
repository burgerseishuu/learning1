def checker(number):
    try:
        return int(number)
    except ValueError:
        print("A number. Please.")
        return None

def operationChecker(operation):
    try:
        op = int(operation)
        if 1 <= op <= 4:
            return op
        else:
            print("Enter a valid option between 1 and 4.")
            return None
    except ValueError:
        print("Enter a valid option.")
        return None

def numberAsk():
    while True:
        number = input("What number do you wanna use? ")
        result = checker(number)
        if result is not None:
            return result

def operationAsk():
    while True:
        operation = input("1. Add | 2. Subtract | 3. Multiply | 4. Divide\nWhich operation do you wish to do? ")
        result = operationChecker(operation)
        if result is not None:
            return result

def askLoop():
    while True:
        ask = input("Yo, how many numbers you trynna process (after the first one)? ")
        result = checker(ask)
        if result is not None and result > 0:
            return result
        print("Enter a positive number.")

def main():
    total_ops = askLoop()
    result = numberAsk()  # First number

    for _ in range(total_ops):
        number = numberAsk()
        operation = operationAsk()

        if operation == 1:
            result += number
        elif operation == 2:
            result -= number
        elif operation == 3:
            result *= number
        elif operation == 4:
            if number == 0:
                print("Cannot divide by zero. Skipping operation.")
                continue
            result /= number

    print(f"{result} is your final number.")

main()
