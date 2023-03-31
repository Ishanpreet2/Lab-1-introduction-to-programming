# Define global constants
PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

# Take input from user
num_pennies = int(input("Enter number of pennies: "))
num_nickels = int(input("Enter number of nickels: "))
num_dimes = int(input("Enter number of dimes: "))
num_quarters = int(input("Enter number of quarters: "))

# Calculate total cents and total dollars
total_cents = (num_pennies * PENNY_VALUE) + (num_nickels * NICKEL_VALUE) + \
              (num_dimes * DIME_VALUE) + (num_quarters * QUARTER_VALUE)
total_dollars = total_cents / PENNIES_IN_DOLLAR

# Check if the amount is exactly one dollar, less than one dollar, or more than one dollar
if total_dollars > 1.0:
    print("Sorry, the amount you entered was more than one dollar.")
elif total_dollars < 1.0:
    print("Sorry, the amount you entered was less than one dollar.")
else:
    print("Congratulations!")
    print("The amount you entered was exactly one dollar!")
    print("You win the game!!")
