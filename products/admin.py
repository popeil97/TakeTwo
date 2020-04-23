from django.contrib import admin
from .models import Product
from django.contrib.auth import get_user_model
# Register your models here.

admin.site.register(Product)


User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    search_fields = ['username']
    class Meta:
        model = User
admin.site.register(User,UserAdmin)