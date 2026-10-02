"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Steve
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
correct_input = True
try:
    user_input = int(input("amount you wanna save every monthly > "))
    if user_input < 1: # doesn't make sense if you wanna save negative amount, thts not saving so it doesn't count
        correct_input = False
except:
    correct_input = False

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
if correct_input:
    yearly = user_input * 12
    interest = yearly * 0.008
    total = yearly + interest
    print(f"yearly amount > {yearly}\n£{total:.2f}")
else:
    print("Invalid amount")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

