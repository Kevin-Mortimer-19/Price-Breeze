from scrape import *
url1 = "https://shopping.rochebros.com/search?search_term="
url2 = "https://www.starmarket.com/shop/search-results.html?q="
product = input("Enter product")

def scrape_product (product):
    search(url1 + product)
    search(url2 + product)
