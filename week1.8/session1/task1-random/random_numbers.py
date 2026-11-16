import random, math

# Get user to input how many random numbers they want
amount = input('get me number > ')
if not amount.isdigit():
    exit()
for i in range(int(amount)):
    #print(math.floor(random.random() * 10))
    print(random.randrange(10))
# Generate this many random numbers

# Write the random numbers to a file named random.txt, one number per line
