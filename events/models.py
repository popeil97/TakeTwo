from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    location = models.CharField(max_length=255,blank=True,null=True)
    university = models.CharField(max_length=255,blank=True,null=True)


    def get_absolute_url(self):
        return f"/events/{self.id}"

    def get_delete_url(self):
        return f"/events/delete/{self.id}"

    def __str__(self):
        return self.title
