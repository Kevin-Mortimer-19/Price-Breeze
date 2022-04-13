from scrape import *
from sort import *

url1 = "https://shopping.rochebros.com/search?search_term="
url2 = "https://www.starmarket.com/shop/search-results.html?q="
product = input("Enter product")

def scrape_product (product):
    data1 = search(url1 + product)
    data2 = search(url2 + product)
    dataTotal = data1 + data2

def sort_price_low_high (data):
    return sort_great_least(data['price'])

def sort_price_high_low (data):
    return sort_least_great(data['price'])

print(scrape_product(product))