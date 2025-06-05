import csv
import os
from datetime import datetime
import pandas as pd

CSV_FILE = "exercise.csv"
HEADERS = ["date", "exercise", "sets", "reps", "weight"]

# Ensure CSV file exists with headers
if not os.path.isfile(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)

# Load file into DataFrame
df = pd.read_csv(CSV_FILE)

def userChooses():
    while True:
        optionChoose = option()
        choosing(optionChoose)

def option():
    while True:
        try:
            optionChoose = int(input("\n1. Log Workout\n2. View Records\n3. Exit\nWhat do you wish to do? "))
            if optionChoose in [1, 2, 3]:
                return optionChoose
            else:
                print("Option must be 1, 2, or 3.")
        except ValueError:
            print("Enter a valid number (1 - 3).")

def choosing(choice):
    if choice == 1:
        newWorkout()
    elif choice == 2:
        viewData()
    elif choice == 3:
        print("Exiting. Goodbye.")
        exit()

# Function to log new workout of the day
def newWorkout():
    date = datetime.now().strftime("%d-%m-%Y")
    entry_count = 0  # Ensure at least 1 entry is logged

    while True:
        if entry_count == 0:
            exercise = input("\nWhich exercise did you do? ").strip().lower()
        else:
            exercise = input("\nWhich exercise did you do? (or type 'exit' to finish) ").strip().lower()
            if exercise == "exit":
                break

        sets = addData("sets")
        reps = addData("reps")
        weight = addData("weight")

        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, exercise, sets, reps, weight])

        entry_count += 1
        print(f"Logged {entry_count} exercise(s) for {date}.")

def addData(field):
    while True:
        try:
            value = int(input(f"How many {field}? "))
            return value
        except ValueError:
            print("Please enter a valid integer.")

# View X day record
def viewData():
    df = pd.read_csv(CSV_FILE)  # Reload in case new data added
    if df.shape[0] == 0:
        print("No data exists.")
        return

    while True:
        askDate = input("\nEnter the date to view (DD-MM-YYYY): ").strip()
        try:
            datetime.strptime(askDate, "%d-%m-%Y")
            break
        except ValueError:
            print("Please enter a valid date format (DD-MM-YYYY).")

    requestedData = df[df["date"] == askDate]

    if requestedData.empty:
        print(f"No workouts found for {askDate}.")
    else:
        print(f"\nWorkouts on {askDate}:\n")
        print(requestedData.to_string(index=False))

# Run the program
if __name__ == "__main__":
    print("=== Workout Logger ===")
    userChooses()
