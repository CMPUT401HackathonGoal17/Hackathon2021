from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    karma = models.IntegerField(default=0)
    comrades = models.IntegerField(default=10)