# Electricity Cost Calculator
# This program asks how many hours a fridge was running,
# and estimates the electricity cost.

print("Welcome to the Electricity Cost Calculator!")  # Task 1 Add project folder and initial app.py with welcome message

# Task 2 — Ask user for input: Add user input prompt for fridge running hours
hours_input = input("How many hours was your fridge turned on today? ")

# Task 5 — Simple error handling: Add basic error handling for non-numeric input
try:
    hours = float(hours_input)  # Task 3 — Convert input to number
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

# Task 3 — Perform a calculation: Add electricity usage and cost calculation
# Assume the fridge uses 0.1 kWh per hour and electricity costs $0.15 per kWh
kwh_used = hours * 0.1
cost = kwh_used * 0.15

# Task 4 — Display result: Add formatted output displaying electricity usage and cost
print(f"\nYour fridge used about {kwh_used:.2f} kWh today.")
print(f"Estimated electricity cost: ${cost:.2f}")

# Task 6 — Clean and final program: Clean up code and add comments to finalize program
