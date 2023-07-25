from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    img_url = models.CharField(max_length=10000)


class Offers(models.Model):
    code = models.CharField(max_length=15)
    description = models.CharField(max_length=500)
    discounts = models.FloatField()

