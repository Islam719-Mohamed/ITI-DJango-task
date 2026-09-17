from django.db import models

# Create your models here.
class tracks(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=True)
    