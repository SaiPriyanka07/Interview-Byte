from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.


class User(AbstractUser):
	email = models.TextField(default=None, null=False)
	password = models.TextField(default=None, null=False)
	fullname = models.TextField(default="", null=True)
	interviwer = models.BooleanField(defaulf=True, null=False)
	resume = models.TextField(default=None, null=False)


class Interviews(models.Model):
	interviwer = models.ForeignKey(User, on_delete = models.CASCADE, defaulf=None, null=False)
	interviwee = models.ForeignKey(User, on_delete = models.CASCADE, defaulf=None, null=False)
	interview_from = models.DateTimeField(default=None, null=False)
	interview_to = models.DateTimeField(default=None, null=False)

