from django.db import models

# Create your models here.

class weblogindb(models.Model):
    UNAME = models.CharField(max_length=100, null=True, blank=True)
    EMAIL = models.EmailField(blank=True, null=True)
    PASSWRD = models.CharField(max_length=50, null=True, blank=True)
    CMFPASSWRD = models.CharField(max_length=50, null=True, blank=True)

class reviewdb(models.Model):
    NAME = models.CharField(max_length=50, null=True, blank=True)
    COUNTRY = models.CharField(max_length=50, null=True, blank=True)
    FEEDBACK = models.CharField(max_length=200, null=True, blank=True)

