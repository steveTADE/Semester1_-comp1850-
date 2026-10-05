# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aires",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["hong kong"] = "hot garbage"

# Display all the keys
print(rivers.keys())

# Display all the values
print(rivers.items())

# Display all the key:value pairs, as tuples
print(rivers)

# Delete an entry from the rivers database
rivers.clear()