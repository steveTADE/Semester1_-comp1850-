# See README.md for instructions on what to do this program

import random

random.seed(10)

num1 = random.randint(1, 255)
num2 = random.randint(1, 255)
num3 = random.randint(1, 255)

print('\x1b[38;2;{};{};{}mhello world'.format(num1, num2, num3))
