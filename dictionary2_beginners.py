# Your expenses dictionary
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Partner's expenses dictionary
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses for each person
total_your_expenses = sum(your_expenses.values())
total_partner_expenses = sum(partner_expenses.values())

# Determine who spent more
if total_your_expenses > total_partner_expenses:
    spender = "You"
    amount_difference = total_your_expenses - total_partner_expenses
else:
    spender = "Your partner"
    amount_difference = total_partner_expenses - total_your_expenses

# Find the expense category with the most significant difference
significant_difference_category = None
max_difference = 0

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > max_difference:
        max_difference = difference
        significant_difference_category = category

# Display the results
print(f"Total your expenses: {total_your_expenses}")
print(f"Total partner expenses: {total_partner_expenses}")
print(f"{spender} spent more by {amount_difference}.")
print(f"The largest difference is in {significant_difference_category} with a difference of {max_difference}.")
