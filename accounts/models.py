from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    is_insurance = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)


class Insurance(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )


class Client(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
