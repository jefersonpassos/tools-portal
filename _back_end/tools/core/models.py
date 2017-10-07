from django.db import models

# Create your models here.

class Tools(models.Model):

    title = models.CharField(max_length=255)
    url = models.CharField(max_length=2500)
    description = models.TextField(max_length=None)