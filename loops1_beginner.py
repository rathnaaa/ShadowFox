import random

# Number of rolls
num_rolls = 20

# Initialize counters
count_six = 0
count_one = 0
count_two_sixes_in_a_row = 0
previous_roll = None  # Track the previous roll for consecutive sixes

# Simulate rolling the die
for _ in range(num_rolls):
    roll = random.randint(1, 6)  # Roll a six-sided die
    
    # Count the number of 6s
    if roll == 6:
        count_six += 1
        # Check for two 6s in a row
        if previous_roll == 6:
            count_two_sixes_in_a_row += 1
    # Count the number of 1s
    elif roll == 1:
        count_one += 1
    
    # Update the previous roll
    previous_roll = roll

# Print statistics
print("Number of times a 6 was rolled:", count_six)
print("Number of times a 1 was rolled:", count_one)
print("Number of times two 6s were rolled in a row:", count_two_sixes_in_a_row)
