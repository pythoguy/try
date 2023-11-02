from django.db import models

# Create your models here.
class ContactU(models.Model):
    Name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    Email = models.CharField(max_length=50)  
    message = models.TextField()

class UserData(models.Model):
    username = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=500)