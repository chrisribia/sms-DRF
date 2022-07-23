from datetime import datetime
from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime
import random


now = datetime.now()

class UserAccountManger(BaseUserManager):
    def create_user(self,email,name,password = None):
        if not email:
            raise ValueError("user must have an email") 
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save()
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserAccountManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE) 
    parent_name = models.CharField(max_length=255,default="")
    DOB = models.DateField(default=timezone.now)
    date_admitted = models.DateField(default=timezone.now)
    previous_School = models.CharField(max_length=255, default="")
    EntryScore = models.IntegerField( default=0)
    comment = models.TextField(max_length=255, default="")
    RegistrationNum = models.CharField(max_length=255,unique = True, default=random.random())


    def __str__(self):
        return f'{self.user.name} Profile'
     

 
