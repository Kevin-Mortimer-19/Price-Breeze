
from audioop import reverse
from cmath import sqrt


#sort by price

def sort_great_least_price (array):
#most expensive to least
    return sorted(array, key=lambda x:x['price'], reverse=True)

def sort_least_great_price (array):
#least expensive to most
     return sorted(array, key=lambda x:x['price'])


#sort by product name

def sort_great_least_product_name (array):
#from Z to A
    return sorted(array, key=lambda x:x['prod_name'], reverse=True)

def sort_least_great_product_name (array):
#from A to Z
     return sorted(array, key=lambda x:x['prod_name'])


#sort by store name

def sort_great_least_store (array):
#from Z to A
    return sorted(array, key=lambda x:x['store'], reverse=True)

def sort_least_great_store (array):
#from A to Z
     return sorted(array, key=lambda x:x['store'])
