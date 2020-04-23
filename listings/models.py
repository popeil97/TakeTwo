from django.db import models

# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    location = models.CharField(max_length=255,blank=True,null=True)
    university = models.CharField(max_length=255,blank=True,null=True)


    def get_absolute_url(self):
        return f"/listings/{self.id}"

    def get_delete_url(self):
        return f"/listings/delete/{self.id}"