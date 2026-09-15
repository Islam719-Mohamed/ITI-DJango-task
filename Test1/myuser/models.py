from django.db import models

# Create your models here.
class user(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=50, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    birthdate = models.DateField()
    password = models.CharField(max_length=50)