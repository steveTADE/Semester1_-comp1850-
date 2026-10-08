# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

# we will use this as print output and use format to fill in the things
output  = """Minimum = {}
Maximum = {}
Mean = {}
Median = {}"""
cond = True
try:
    number_arr = read_numbers()
    cond = number_arr != [] # i can compress the code further if i do this to avoid using if <condition> : ... line
except:
    cond = False

if not cond:
    sys.exit("Error: no numbers provided")

# can use the python built-in functions like max min but i think its gonna be a BIT less efficient than this
number_arr.sort();
length_arr = len(number_arr);
minimum    = number_arr[0];              # since its sorted this will always return the smallest
maximum    = number_arr[length_arr - 1]; # and this will return the biggest in the array
mean       = sum(number_arr) / length_arr;
if length_arr%2 == 0: # even number
    median = (number_arr[int(length_arr/2)] + number_arr[int(length_arr/2) -1]) / 2
else:
    median = number_arr[int(length_arr/2)];

print(output.format(minimum, maximum, mean, median))