from django.db import models

# Create your models here.

class Product(models.Model):

    id = models.IntegerField(primary_key=True)
    cost = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)

    def __str__(self): 
        return self.title

class Bin(models.Model):

    id = models.IntegerField(primary_key=True)
    cost = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)

    def __str__(self): 
        return self.title