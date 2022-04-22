from breeze.scrape import *

#function to process input from search bar on page
def getInput(req):
    productItem = req
    return productItem

#function to scrape products - web scraper
def scrape_product(productItem):
    #url to search with + user input product
    urlPT1 = "https://www.google.com/search?q="
    urlPT2 = "&rlz=1C1MMCH_enUS934US934&source=lnms&tbm=shop&sa=X&ved=2ahUKEwi5ocPzn5P3AhVWg4kEHdz0AiMQ_AUoAnoECAIQBA&biw=1858&bih=1097"
    
    url = urlPT1 + productItem + urlPT2
    output = search(url)