from django.db import models

# Create your models here.
class Story(models.Model):
    
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False)
    media = models.CharField(max_length=100)