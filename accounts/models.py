from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,username,password=None,is_active=True,is_staff=False,is_admin=False):
        if not username:
            raise ValueError("Users must have a username alias")
        user = self.model(
            username = username
        )
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self,username,password=None):

        staff_user = self.create_user(
            username = username,
            password=password,
            is_active = True,
            is_staff = True
        )

        return staff_user

    def create_superuser(self,username,password=None):
        if not username:
            raise ValueError("Users must have a username alias")

        super_user = self.create_user(
            username = username,
            password = password,
            is_active = True,
            is_staff = True,
            is_admin = True
        )

        return super_user

class User(AbstractBaseUser):
    username = models.CharField(max_length=255,unique=True)
    staff = models.BooleanField(default=False)
    company = models.CharField(max_length=255,null=True,blank=True)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin