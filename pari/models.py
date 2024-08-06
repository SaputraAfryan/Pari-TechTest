from django.db import models

# Create your models here.
class Books(models.Model):
    author = models.CharField(max_length=85)
    year = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=85)
    city = models.CharField(max_length=85)
    publisher = models.CharField(max_length=85)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
