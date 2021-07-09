from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.

class custom_user(models.Model):
    #user = models.OneToOneField(User,on_delete=CASCADE)
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    group = models.CharField(max_length=1, blank=True)
    profile_pic = models.ImageField(upload_to='uploads/',blank=True)
    
    def __str__(self):
        return self.username