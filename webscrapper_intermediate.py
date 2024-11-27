import requests
from bs4 import BeautifulSoup

# Step 1: Send an HTTP request to a website
url = 'https://example.com'  # Replace with the website you want to scrape
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Step 2: Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Extract specific data from the page (e.g., all heading tags)
    headings = soup.find_all(['h1', 'h2', 'h3'])  # Find all h1, h2, and h3 tags

    # Step 4: Print the extracted data
    print("Headings found on the page:")
    for heading in headings:
        print(heading.text.strip())  # Print each heading text, removing extra whitespace

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
