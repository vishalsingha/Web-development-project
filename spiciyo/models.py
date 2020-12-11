from django.db import models

# Create your models here.

class cards(models.Model):
    name = models.CharField(max_length=100)
    des  = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='pics')

class slider_card(models.Model):
    name_s = models.CharField(max_length=100)
    price_s = models.IntegerField()
    image_s = models.ImageField(upload_to='pics')

class call_request(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.ImageField(max_length=10)
    message = models.CharField(max_length=500)

class newsletter(models.Model):
    email = models.EmailField()
