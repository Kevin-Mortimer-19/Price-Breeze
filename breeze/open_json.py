from unicodedata import category
import pandas
import numpy
import json
from breeze.sort import *
from IPython.display import HTML
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
    df = pandas.DataFrame(data)
    return printTable(df)
    #dfg = df.groupby(['title','category','price'], sort=False).sum()
    #table = dfg.to_html(filepath2,)

    #return table

def highTablePrice():
#sorted data by price highest to lowest 
    data_sorted_greatest = sort_great_least_price(data)
    df = pandas.DataFrame(data_sorted_greatest)
    return printTable(df)
    #dfg = df.groupby(['title','category','price'], sort=False).sum()
    #table = dfg.to_html(filepath2,)

    #return table

def lowTablePrice():
#sorted data by price lowest to highest 
    data_sorted_lowest = sort_least_great_price(data)
    df = pandas.DataFrame(data_sorted_lowest)
    return printTable(df)
    #dfg = df.groupby(['title','category','price'], sort=False).sum()
    #table = dfg.to_html(filepath2,)

    #return table

def highTableName():
#sorted data by price highest to lowest 
    data_sorted_greatest = sort_great_least_product_name(data)
    df = pandas.DataFrame(data_sorted_greatest)
    return printTable(df)
    #dfg = df.groupby(['title','category','price'], sort=False).sum()
    #table = dfg.to_html(filepath2,)

    #return table

def lowTableName():
#sorted data by price lowest to highest 
    data_sorted_lowest = sort_least_great_product_name(data)
    df = pandas.DataFrame(data_sorted_lowest)
    return printTable(df)
    #dfg = df.groupby(['title','category','price'], sort=False).sum()
    #table = dfg.to_html(filepath2,)

    #return table

def highTableStore():
#sorted data by price highest to lowest 
    data_sorted_greatest = sort_great_least_store(data)
    df = pandas.DataFrame(data_sorted_greatest)
    return printTable(df)
    #dfg = df.groupby(['title','category','price'], sort=False).sum()
    #table = dfg.to_html(filepath2,)

    #return table

def lowTableStore():
#sorted data by price lowest to highest 
    data_sorted_lowest = sort_least_great_store(data)
    df = pandas.DataFrame(data_sorted_lowest)
    return printTable(df)
    #dfg = df.groupby(['title','category','price'], sort=False).sum()
    #table = dfg.to_html(filepath2,)

    #return table


def printTable(df):
    dfg = df.groupby(['prod_name','store','price'], sort=False).sum()
    table = dfg.to_html(filepath2,)

    return table


# Closing file
f.close()