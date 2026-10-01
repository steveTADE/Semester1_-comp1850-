# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:
num_of_input = 2 # you can increase or decrease the number of input
output = 1 # if this is zero the entire code will not work
for i in range(num_of_input):
    tmp_input = input("enter a number > ")
    while True: # catches error if the user input something that is not a number
        try:
            tmp_input = int(tmp_input) 
            break # this will only if the line above worked
        except:
            tmp_input = input("enter a number > ")

    output *= tmp_input

print(output)

# Ask a user to enter two numbers (one per input)

# multiply those numbers together

# print out the result

# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!