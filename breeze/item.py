# SingleItem class
#
# parameters:
#   title: the name of the product
#   price: the price (as string)
#   location: store or website where the product can be found
#
# SingleItem is used to store relevant info for displaying search results, and for adding Items to the user's ShoppingList

class SingleItem:
    def __init__(self, title, price, location):
        self.title = title
        self.price = price
        self.location = location