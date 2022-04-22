from bs4 import BeautifulSoup
from requests_html import HTMLSession
from breeze.open_json import *
import json
from breeze.open_json import *

def search(url):

    print("inside search function")
    s = HTMLSession()
    source = s.get(url)
    # source.html.render(sleep=10) #used for testing purposes

    soup = BeautifulSoup(source.text, 'html.parser')

    #grabs product_name, price, storename, and links
    prod_name = soup.find_all('h4', class_='Xjkr3b')
    prices = soup.find_all('span', class_="a8Pemb OFFNJ")
    store = soup.find_all('div', class_='aULzUe IuHnof')
    links = soup.find_all('a', class_="shntl", href=True)

    #addding web scraped data to arrays
    prodArr, priceArr, storeArr, linksArr = [], [], [], []

    for line in prod_name:
        prodArr.append(line.getText(strip=True))

    for line in prices:
        priceVal = line.getText(strip=True)
        priceNum1 = priceVal.replace("$","")
        priceNum2 = float(priceNum1.replace(",", ""))
        priceArr.append(priceNum2)

    for line in store:
        storeArr.append(line.getText(strip=True))

    for line in links:
        for a in links:
            linksArr.append(a['href'])

    data = [{"prod_name": i, "price": p, "store": s, "link": l}
            for i, p, s, l in zip(prodArr, priceArr, storeArr, linksArr)]

    #dump data out to JSON file
    with open("breeze\products.json", 'w') as outfile:
        json.dump(data, outfile, indent=2)

    #calling function to open JSON file
    openJSON()