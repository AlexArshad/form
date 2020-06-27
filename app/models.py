from __future__ import unicode_literals
from django.db import connection
from django.db import models

# Create your models here.

class Student(models.Model):
    eid = models.CharField(unique=True, max_length=20)
    ename = models.CharField(unique=False, max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(unique=False, max_length=15)

    class Meta:
        managed = True
        db_table = 'student_data'