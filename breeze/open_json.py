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

def startTable():
    df = pandas.DataFrame(data)
    dfg = df.groupby(['title','category','price'], sort=False).sum()
    table = dfg.to_html(filepath2,)
    print("it worked")
    return table

def highTable():
#sorted data by price highest to lowest 
    data_sorted_greatest = sort_great_least_price(data)
    df = pandas.DataFrame(data_sorted_greatest)
    dfg = df.groupby(['title','category','price'], sort=False).sum()
    table = dfg.to_html(filepath2,)
    print("it worked")
    return table

def lowTable():
#sorted data by price lowest to highest 
    data_sorted_lowest = sort_least_great_price(data)
    df = pandas.DataFrame(data_sorted_lowest)
    dfg = df.groupby(['title','category','price'], sort=False).sum()
    table = dfg.to_html(filepath2,)
    print("it worked")
    return table

# Closing file
f.close()