from django.contrib import admin
from .models import User, ShoppingList, Item

admin.site.register(User)
admin.site.register(ShoppingList)
admin.site.register(Item)
