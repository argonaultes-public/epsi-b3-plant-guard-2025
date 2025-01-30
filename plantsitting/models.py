from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Owner(User):
    avatar_url = models.CharField(max_length=100, null=True)
    timezone = models.CharField(max_length=50, default='Europe/Paris')

    def __str__(self):
        return self.email

class Plant(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    ltn = models.FloatField(default=51.5)
    lgt = models.FloatField(default=-0.09)

    def __str__(self):
        return self.name
