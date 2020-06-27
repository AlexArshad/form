from __future__ import unicode_literals
from django.db import connection
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Main(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name 

    
class AuthUser(models.Model):

    username = models.CharField(unique=True, max_length=30)
    email = models.EmailField(unique=True, max_length=50)
    password = models.CharField(unique=False, max_length=20)

    class Meta: 
        managed = False
        db_table = "auth_user"


        