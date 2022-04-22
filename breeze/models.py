from django.db import models
from django.contrib.auth.models import User
import uuid
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

#class User(models.Model):
    #user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique User ID')
    #username = models.CharField(max_length=50)
    #password = models.CharField(max_length=50)
    #default_location = models.CharField(max_length=50)

#class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class ShoppingList(models.Model):
    #list_id = models.IntegerField()
    #userid = User.user_id
    #userid = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    userid = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
class Item(models.Model): 
    item_id = models.IntegerField()
    userid = models.ForeignKey('ShoppingList', on_delete=models.CASCADE, null=True)
    item_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50)
    
    
