import requests
from bs4 import BeautifulSoup

# Select website to scrape
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
books = soup.find_all("article")

# Extract information from the website
for book in books:
    title = book.h3.a["title"]
    rating = book.select_one("p.star-rating")["class"][1]
    print(f"The book name is: {title} and the rating is: {rating}")