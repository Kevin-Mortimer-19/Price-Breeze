import json
from sort import *

# Opening JSON file
f = open('products.json')

# returns JSON object as
# a list of dictionaries
data = json.load(f)

#sorted data by price
data_sorted_greatest = sort_great_least_price(data)
data_sorted_lowest = sort_least_great_price(data)

# Closing file
f.close()