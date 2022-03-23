from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.IntField(min_length=1)
    username = models.CharField(max_length=50,min_length=1)
    password = models.CharField(max_length=50,min_length=1)
    default_location = models.CharField(max_length=50,min_length=1)
    
class ShoppingList(models.Model,User):
    list_id = models.IntField(min_length=1)
    userid = User.user_id
    
class Item(models.Model,ShoppingList): 
    item_id = models.IntField(min_length=1)
    listid = ShoppingList.list_id
    item_name = models.CharField(max_length=50,min_length=1)
    location = models.CharField(max_length=50,min_length=1)
    
    
    