from django.db import models
from products.models import Product

# Create your models here.
class CartItem(models.Model):
    username = models.CharField(max_length=120)
    productID = models.IntegerField()

