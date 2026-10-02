# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:
output = 1 # if this is zero the entire code will not work
tmp_input1 = input("enter a number > ")
try:
    tmp_input1 = int(tmp_input1) 
except:
    print("That is not a number")
    exit()
output *= tmp_input1

tmp_input1 = input("enter a number > ")
try:
    tmp_input1 = int(tmp_input1) 
except:
    print("That is not a number")
    exit()
output *= tmp_input1

print(output)

# Ask a user to enter two numbers (one per input)

# multiply those numbers together

# print out the result

# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!