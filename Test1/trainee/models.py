from django.db import models

# Create your models here.
class trainees(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phono = models.IntegerField(unique=True)
    pfp = models.ImageField(upload_to='trainee/images', blank=True)