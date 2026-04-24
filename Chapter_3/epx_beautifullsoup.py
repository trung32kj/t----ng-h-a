from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

products = soup.find_all("article", class_="product_pod")

data_books = []   # list rỗng để lưu dữ liệu

for book in products:
    name = book.h3.a["title"]

    price = book.find("p", class_="price_color").text.replace("£", "")

    star_rating = book.find("p", class_="star-rating")["class"][1]

    in_stock = book.find("p", class_="instock availability").text.strip()

    dict_data = {
        "name": name,
        "price": price,
        "star_rating": star_rating,
        "in_stock": in_stock
    }

    data_books.append(dict_data)
    

df_input = pd.DataFrame(data_books)
print(df_input)
print()


print("------------------")