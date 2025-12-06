from django.db import models

# Create your models here.
class datas(models.Model): 
    head = models.CharField(max_length=100)
    note =models.TextField(max_length=500)
