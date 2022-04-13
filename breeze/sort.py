
from audioop import reverse
from cmath import sqrt


def sort_great_least_price (array):
    return sorted(array, key=lambda x:x['price'], reverse=True)

def sort_least_great_price (array):
     return sorted(array, key=lambda x:x['price'])

def distance_calc (x1, y1, x2, y2):
    xFin = (x1*x1) + (x2*x2)
    yFin = (y1*y1) + (y2*y2)
    return sqrt(xFin + yFin)
    
import json
 
# Opening JSON file
f = open('products.json')


# returns JSON object as
# a dictionary
data = json.load(f)
data = sort_great_least_price(data)
print(data)

# Closing file
f.close()