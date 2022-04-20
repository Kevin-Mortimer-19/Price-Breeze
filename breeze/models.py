from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique User ID')
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    default_location = models.CharField(max_length=50)
    
class ShoppingList(models.Model):
    list_id = models.IntegerField()
    userid = User.user_id
    userid = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    
class Item(models.Model): 
    item_id = models.IntegerField()
    userid = models.ForeignKey('ShoppingList', on_delete=models.SET_NULL, null=True)
    item_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    
    
