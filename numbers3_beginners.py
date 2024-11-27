# Question 3
distance = 490  # Distance in meters
time_minutes = 7  # Time in minutes
time_seconds = time_minutes * 60  # Convert time to seconds

# Calculate speed and print without decimal points
speed_mps = int(distance / time_seconds)
print("Speed in meters per second:", speed_mps)  # Without decimal point
