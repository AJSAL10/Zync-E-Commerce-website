from django.db import models

# Create your models here.

class admindb(models.Model):
    NAME = models.CharField(max_length=50, null=True, blank=True)
    EMAIL = models.ImageField(null=True, blank=True)
    NUMBER = models.IntegerField( null=True, blank=True)
    USERNAME = models.CharField(max_length=50, null=True, blank=True)
    PASSWORD = models.CharField(max_length=50, null=True, blank=True)
    IMAGE = models.ImageField(upload_to="profile", null=True, blank=True)

class categorydb(models.Model):
    NAME = models.CharField(max_length=50, null=True, blank=True)
    DISCRIPTION = models.CharField(max_length=50, null=True, blank=True)
    IMAGE = models.ImageField(upload_to="category", null=True, blank=True)

class productdb(models.Model):
    NAME = models.CharField(max_length=100, null=True, blank=True)
    CATEGORY = models.CharField(max_length=100, null=True, blank=True)
    PRIZE = models.IntegerField(null=True, blank=True)
    QUANTITY = models.IntegerField(null=True, blank=True)
    SPECIFICATION = models.CharField(max_length=500, null=True, blank=True)
    IMAGE = models.ImageField(upload_to="product", null=True, blank=True)

class gallerydb(models.Model):
    NAME = models.CharField(max_length=100,blank=True, null=True)
    IMAGE = models.ImageField(upload_to="Gallery",null=True, blank=True)

class contactusdb(models.Model):
    NAME = models.CharField(max_length=50, null=True, blank=True)
    EMAIL = models.EmailField(null=True, blank=True)
    SUBJECT = models.CharField(max_length=100, blank=True, null=True)
    MESSAGE = models.CharField(max_length=500, null=True, blank=True)

class cartdb(models.Model):
    NAME = models.CharField(max_length=50, null=True, blank=True)
    PDCTNAME = models.CharField(max_length=50, null=True, blank=True)
    CATEGORY = models.CharField(max_length=100, null=True, blank=True)
    PRIZE = models.IntegerField(null=True, blank=True)
    QUANTITY = models.IntegerField(null=True, blank=True)