# List of friends' names
friends = ["Aditya", "Nina", "Sam", "Jonathan", "Emily"]

# Create a list of tuples with each friend's name and the length of their name
name_lengths = [(name, len(name)) for name in friends]

# Print the result
print(name_lengths)
