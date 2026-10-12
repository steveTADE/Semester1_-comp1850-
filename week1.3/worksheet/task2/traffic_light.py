"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Steve
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

sys_time = 0
max_time = int(input())  # read an integer number of steps (>0)

state = "red"

while True:
    for key, number in states.items():
        for _i in range(number):
            if sys_time > max_time:
                exit()
            print(f"Time {sys_time:03} State {key}")
            sys_time += 1

# Simulate the traffic light system up to time=max_time in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14