from django.db import models

# Create your models here.
class post(models.Model):
    titel = models.CharField(max_length=100)
    dec = models.TextField(max_length=300)
