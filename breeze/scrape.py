# import library
from bs4 import BeautifulSoup
import requests
# Request to website and download HTML contents

def search(url):
    req=requests.get(url)
    content=req.text
    soup=BeautifulSoup(content)
    raw=soup.findAll('script')[3].text
    page=pd.read_json(raw.split("window.pageData=")[1],orient='records')
    #Store data
    for item in page.loc['listItems','mods']:
        brand_name.append(item['brandName'])
        price.append(item['price'])
        location.append(item['location'])
        description.append(ifnull(item['description'],0))
        rating_score.append(ifnull(item['ratingScore'],0))
    #save data into an output
    output=pd.DataFrame({'brandName':brand_name,'price':price,'location':location,'description':description,'rating score':rating_score})
    for i in range(1,50):
        time.sleep(max(random.gauss(5,1),2))
        print('page'+str(i))
        payload['page']=i
        req=requests.get(url,params=payload)
        content=req.text
        soup=BeautifulSoup(content)
        raw=soup.findAll('script')[3].text
        page=pd.read_json(raw.split("window.pageData=")[1],orient='records')
        for item in page.loc['listItems','mods']:
            brand_name.append(item['brandName'])
            price.append(item['price'])
            location.append(item['location'])
            description.append(ifnull(item['description'],0))
            rating_score.append(ifnull(item['ratingScore'],0))