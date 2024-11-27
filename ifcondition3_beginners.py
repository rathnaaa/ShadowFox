# Program to check if two cities belong to the same country

# Define the lists of cities for each country
countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

# Get user input for the two cities
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Function to find the country of a city
def find_country(city):
    for country, cities in countries.items():
        if city in cities:
            return country
    return None

# Find the countries of the two cities
country1 = find_country(city1)
country2 = find_country(city2)

# Check if both cities belong to the same country and print the result
if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the list")
