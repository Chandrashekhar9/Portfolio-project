from django.db import models

# Create your models here.
class jobs(models.Model):
    images = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)


