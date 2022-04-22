from unicodedata import category
import pandas
import numpy
import json
from breeze.sort import *
#from IPython.display import HTML
from breeze.item import Item
import os


filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'products.json')
filepath2 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates/result.html')
# Opening JSON file
f = open(filepath,)

# returns JSON object as
# a list of dictionaries
data = json.load(f)

def updateTable():
    f = open(filepath,)
    data = json.load(f)


def startTable():
#prints table at beginning when starting search page
    df = pandas.DataFrame(data)
    return printTable(df)

def highTablePrice():
#prints sorted data by price highest to lowest 
    data_sorted_greatest = sort_great_least_price(data)
    df = pandas.DataFrame(data_sorted_greatest)
    return printTable(df)

def lowTablePrice():
#prints sorted data by price lowest to highest 
    data_sorted_lowest = sort_least_great_price(data)
    df = pandas.DataFrame(data_sorted_lowest)
    return printTable(df)

def highTableName():
#prints sorted data by product name form Z-A 
    data_sorted_greatest = sort_great_least_product_name(data)
    df = pandas.DataFrame(data_sorted_greatest)
    return printTable(df)

def lowTableName():
#prints sorted data by product name from A-Z
    data_sorted_lowest = sort_least_great_product_name(data)
    df = pandas.DataFrame(data_sorted_lowest)
    return printTable(df)

def highTableStore():
#prints sorted data by store name from Z-A
    data_sorted_greatest = sort_great_least_store(data)
    df = pandas.DataFrame(data_sorted_greatest)
    return printTable(df)

def lowTableStore():
#prints sorted data by store name from A-Z
    data_sorted_lowest = sort_least_great_store(data)
    df = pandas.DataFrame(data_sorted_lowest)
    return printTable(df)

def printTableAlt(df):
#prints any dataframe to html table
    dfg = df.groupby(['prod_name','store','price'], sort=False).sum()
    table = dfg.to_html(filepath2,)

    return table

def startTableAlt():
    df = pandas.DataFrame(data)
    return printTable(df)

def printTable(df):

    results = []
    for index in df.index:
        #entry = Item(row['title'], row['price'], row['description'], row['location'])
        #entry = Item(df['title'][index], df['price'][index], df['description'][index], df['location'][index])
        entry = Item(df['prod_name'][index], df['price'][index], df['description'][index], df['store'][index])
        results.append(entry)
    return results
    #for ind in df.index:
     #print(df['Name'][ind], df['Stream'][ind])

# Closing file
f.close()