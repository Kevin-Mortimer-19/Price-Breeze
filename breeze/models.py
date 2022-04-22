from django.db import models
from django.contrib.auth.models import User
import uuid
from django.conf import settings
from django.contrib.auth import get_user_model

# Shopping List model
# Each User has a unique ShoppingList, and each ShoppingList contains zero or many Items
    
class ShoppingList(models.Model):
    userid = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

# Item model
# Each Item must belong to a ShoppingList, and has fields for name, price, and location
    
class Item(models.Model): 
    item_id = models.IntegerField()
    userid = models.ForeignKey('ShoppingList', on_delete=models.CASCADE, null=True)
    item_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50)