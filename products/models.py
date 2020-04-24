from django.db import models
from accounts.models import User
from events.models import Event
from TakeTwo import settings
import os
# Create your models here.
def get_image_path(instance, filename):
    return os.path.join('/photos', str(instance.id), filename)

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=10000)
    image = models.CharField(max_length=120)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    sold_at = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    daily_deal = models.BooleanField(default=False)


    def get_absolute_url(self):
        return f"/products/{self.id}"

    def get_delete_url(self):
        return f"/products/delete/{self.id}"

    def get_cart_url(self):
        return f"/cart/{self.id}"
