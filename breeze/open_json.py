from unicodedata import category
import pandas
import numpy
import json
from breeze.sort import *
from IPython.display import HTML
from breeze.item import Item
import os


filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'products.json')
filepath2 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates/result.html')
# Opening JSON file
f = open(filepath,)

# returns JSON object as
# a list of dictionaries
data = json.load(f)

def startTable():
    df = pandas.DataFrame(data)
    return printTable(df)
    #dfg = df.groupby(['title','category','price'], sort=False).sum()
    #table = dfg.to_html(filepath2,)

    #return table

def highTable():
#sorted data by price highest to lowest 
    data_sorted_greatest = sort_great_least_price(data)
    df = pandas.DataFrame(data_sorted_greatest)
    return printTable(df)
    #dfg = df.groupby(['title','category','price'], sort=False).sum()
    #table = dfg.to_html(filepath2,)

    #return table

def lowTable():
#sorted data by price lowest to highest 
    data_sorted_lowest = sort_least_great_price(data)
    df = pandas.DataFrame(data_sorted_lowest)
    return printTable(df)
    #dfg = df.groupby(['title','category','price'], sort=False).sum()
    #table = dfg.to_html(filepath2,)

    #return table


def printTable(df):
    dfg = df.groupby(['title','category','price'], sort=False).sum()
    table = dfg.to_html(filepath2,)

    return table

def startTableAlt():
    df = pandas.DataFrame(data)
    return printTableAlt(df)

def printTableAlt(df):

    results = []
    for index in df.index:
        #entry = Item(row['title'], row['price'], row['description'], row['location'])
        #entry = Item(df['title'][index], df['price'][index], df['description'][index], df['location'][index])
        entry = Item(df['title'][index], df['price'][index], df['description'][index], "sample location")
        results.append(entry)
    return results
    #for ind in df.index:
     #print(df['Name'][ind], df['Stream'][ind])


# Closing file
f.close()