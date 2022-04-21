from scrape import *
from sort import *

#url to search with + user input product
urlPT1 = "https://www.google.com/search?q="
urlPT2 = "&rlz=1C1MMCH_enUS934US934&source=lnms&tbm=shop&sa=X&ved=2ahUKEwi5ocPzn5P3AhVWg4kEHdz0AiMQ_AUoAnoECAIQBA&biw=1858&bih=1097"
product = input("Enter product: ")
url = urlPT1 + product + urlPT2

def scrape_product(product):
    output = search(url)

scrape_product(url)
#print(scrape_product(product))
