# Worksheet 1.3: Task 1

length = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
sequence = [0] * length

for n in range(1, length):
    tmp = sequence[n - 1]
    if (tmp - n) > 0 and (tmp - n) not in sequence:
        sequence[n] = tmp - n
    else:
        sequence[n] = tmp + n


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence