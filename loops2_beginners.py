# Total jumping jacks required
total_jumping_jacks = 100
jumping_jacks_per_set = 10
completed_jumping_jacks = 0

# Loop through each set of 10 jumping jacks
while completed_jumping_jacks < total_jumping_jacks:
    completed_jumping_jacks += jumping_jacks_per_set
    print(f"You completed {completed_jumping_jacks} jumping jacks.")
    
    # If user has completed all jumping jacks, end the workout
    if completed_jumping_jacks >= total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break

    # Ask if the user is tired
    tired_response = input("Are you tired? (yes/y or no/n): ").strip().lower()
    
    if tired_response in ["yes", "y"]:
        # Ask if the user wants to skip remaining sets
        skip_response = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip_response in ["yes", "y"]:
            print(f"You completed a total of {completed_jumping_jacks} jumping jacks.")
            break
    elif tired_response in ["no", "n"]:
        # Calculate and display remaining jumping jacks
        remaining_jumping_jacks = total_jumping_jacks - completed_jumping_jacks
        print(f"{remaining_jumping_jacks} jumping jacks remaining.")
