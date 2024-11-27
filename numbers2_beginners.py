# Question 2
radius = 84  # Radius of the pond in meters
pi_value = 3.14  # Approximate value for π
water_per_square_meter = 1.4  # Liters of water per square meter

# Calculate the area of the pond
pond_area = pi_value * radius ** 2
print("Pond Area:", pond_area)

# Calculate the total amount of water in the pond and remove decimal points
total_water = int(pond_area * water_per_square_meter)
print("Total amount of water in the pond:", total_water)  # Without decimal point
