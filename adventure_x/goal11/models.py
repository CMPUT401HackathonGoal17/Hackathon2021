from django.db import models
from landingpage.models import User

# Create your models here.
class UserGoal11(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)