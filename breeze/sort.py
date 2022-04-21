
from audioop import reverse
from cmath import sqrt


def sort_great_least_price (array):
    return sorted(array, key=lambda x:x['price'], reverse=True)

def sort_least_great_price (array):
     return sorted(array, key=lambda x:x['price'])

def sort_great_least_product_name (array):
    return sorted(array, key=lambda x:x['prod_name'], reverse=True)

def sort_least_great_product_name (array):
     return sorted(array, key=lambda x:x['prod_name'])

def sort_great_least_store (array):
    return sorted(array, key=lambda x:x['store'], reverse=True)

def sort_least_great_store (array):
     return sorted(array, key=lambda x:x['store'])
