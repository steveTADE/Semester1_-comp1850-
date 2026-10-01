"""
num_of_input = 2
output_array = [0] * num_of_input
output = 0
for i in range(num_of_input):
    output_array[i] = int(input("enter a number > "))

output = sum(output_array)
"""
# ask the user to enter number1:
usr_input_1 = int(input("enter a number > "))
    
# ask the user to enter number 2:
usr_input_2 = int(input("enter a number > "))

# calculate the result of adding those numbers together
output = sum([usr_input_1, usr_input_2])

# print out the answer
print(output)
