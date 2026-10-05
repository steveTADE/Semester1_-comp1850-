# Worksheet 1.2: Task 1 Solution
import sys

correct_input = True
# by doing this i can avoid using isdecimal()
try:
    user_input = int(input("enter an integer grade > ")) # only works when user enters an integer and nothing else
    correct_input = 0 <= user_input <= 100 # this will only happen if the user input numbers
except:
    correct_input = False

# catches errors and make sure its in range
if not correct_input: 
    sys.exit("Error: Grade must be an integer between 0 and 100")

# really neat way of doing this, looks clean and works
grade_range_dictionary = { 
    (0  <= user_input <= 39)  : "{} is a fail",
    (40 <= user_input <= 69)  : "{} is a pass",
    (70 <= user_input <= 100) : "{} is a distinction"
} [True]

print(grade_range_dictionary.format(user_input))