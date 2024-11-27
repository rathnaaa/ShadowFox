# Program to determine which country a city belongs to based on predefined lists

# Define the lists of cities for each country
countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

# Get user input for city name
city_name = input("Enter a city name: ")

# Check which country the city belongs to
country_found = None
for country, cities in countries.items():
    if city_name in cities:
        country_found = country
        break

# Output the result
if country_found:
    print(f"{city_name} is in {country_found}")
else:
    print(f"{city_name} is not in the list")
