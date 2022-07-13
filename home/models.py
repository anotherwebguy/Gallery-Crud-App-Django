from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=122)
    url = models.CharField(max_length=300)
    detail = models.TextField()