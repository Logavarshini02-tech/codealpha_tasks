import requests
from bs4 import BeautifulSoup
import csv

# Target URL
url = "https://books.toscrape.com/catalogue/page-1.html"

# Send GET request
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all book items
books = soup.find_all("article", class_="product_pod")

# Create CSV file
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Availability"])

    for book in books:
        # Extract title
        title = book.h3.a["title"]

        # Extract price
        price = book.find("p", class_="price_color").get_text()

        # Extract availability
        availability = book.find("p", class_="instock availability").get_text(strip=True)

        writer.writerow([title, price, availability])

print("✅ Book data saved to books.csv")