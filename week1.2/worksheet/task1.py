# Worksheet 1.2: Task 1 Solution
import sys

cond = True
# by doing this i can avoid using isdecimal()
try:
    user_input = int(input("enter an integer grade > ")) # only works when user enters an integer and nothing else
    cond       = 0 <= user_input <= 100 # this will only happen if the user input numbers
except:
    cond = False

# catches errors and make sure its in range
if not cond: 
    sys.exit("Error: Grade must be an integer between 0 and 100")

# really neat way of doing this, looks clean and works
grade_range_dictionary = { 
    (0  <= user_input <= 39)  : "{} is a Fail",
    (40 <= user_input <= 69)  : "{} is a Pass",
    (70 <= user_input <= 100) : "{} is a Distinction"
} [True]

print(grade_range_dictionary.format(user_input))