#import libraries to request websites html
import requests
from bs4 import BeautifulSoup

#select web site to scrape
response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.content, "html.parser")
books = soup.find_all("article")

#detect the inforamtion i need from website
for book in books:
    title = book.h3.a ["title"]
    rate = book.p["class"][1]
    print(f"the book name is: {title} and rate is: {rate}")

