from django.db import models
from landingpage.models import User

class UserGoal1(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)