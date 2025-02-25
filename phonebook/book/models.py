# models.py
from django.db import models

class crud(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)

    def __str__(self):
        return self.name
