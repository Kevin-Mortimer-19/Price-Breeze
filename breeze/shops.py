from breeze.scrape import *
# from sort import *

# productItem = ""
# url = ""


def getInput(req):
    productItem = req
    print('input grabbed = %s', productItem)
    return productItem
    # product = input("Enter product: ")
    # return product;
    

def scrape_product(productItem):
    #url to search with + user input product
    urlPT1 = "https://www.google.com/search?q="
    urlPT2 = "&rlz=1C1MMCH_enUS934US934&source=lnms&tbm=shop&sa=X&ved=2ahUKEwi5ocPzn5P3AhVWg4kEHdz0AiMQ_AUoAnoECAIQBA&biw=1858&bih=1097"
    
    url = urlPT1 + productItem + urlPT2
    print("product scraped with url = %s ", url)
    output = search(url)


# getInput(product)
# print('input grabbed = %s', product)
# scrape_product(url)
# print("product scraped with url = %s ", url)


#print(scrape_product(product))
