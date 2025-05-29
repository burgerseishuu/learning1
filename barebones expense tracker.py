user = [0] * 6
categories_list = ["Rent", "Food", "Travel", "Electricity", "Water", "Misc"]

def askUserMenu():
    while True:
        userChoice = input("1. Add Expense | 2. View Expenses | 3. Total Spent | 4. Exit\nWhat do you wish to do? ")
        if userChoice.isnumeric():
            userChoice = int(userChoice)
            if 1 <= userChoice <= 4:
                return userChoice
            else:
                print("Valid options are 1 - 4")
        else:
            print("Enter numeric values only")

def categories():
    while True:
        print("Choose a category:")
        for i, name in enumerate(categories_list, 1):
            print(f"{i}. {name}")
        userCategory = input("Which category do you wish to choose? ")
        if userCategory.isnumeric():
            userCategory = int(userCategory)
            if 1 <= userCategory <= 6:
                return userCategory
            else:
                print("Enter values 1 - 6")
        else:
            print("Enter numeric values only")

def addExpenses(userChoosesCategory):
    while True:
        addHowMuch = input("How much do you want to add? ")
        if addHowMuch.isnumeric():
            addHowMuch = int(addHowMuch)
            user[userChoosesCategory - 1] += addHowMuch
            print(f"Added {addHowMuch} to {categories_list[userChoosesCategory - 1]}")
            break
        else:
            print("Enter a valid value")

def viewExpenses():
    print("\nCurrent Expenses:")
    for i in range(6):
        print(f"{i + 1}. {categories_list[i]}: {user[i]}")
    print()

def totalSpent():
    total = sum(user)
    print("\nTotal Spent:", total, "\n")

# Main program loop
while True:
    userChoosesMenu = askUserMenu()
    match userChoosesMenu:
        case 1:
            userChoosesCategory = categories()
            addExpenses(userChoosesCategory)
        case 2:
            viewExpenses()
        case 3:
            totalSpent()
        case 4:
            print("Thank you for choosing us")
            break
