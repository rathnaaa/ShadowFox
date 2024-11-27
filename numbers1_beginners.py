# Question 1
def format_example(value, format_spec):
    return format(value, format_spec)

# Call the function with 145 and 'o' as arguments
result = format_example(145, 'o')
print("Formatted result:", result)  # Expected output: octal representation of 145
