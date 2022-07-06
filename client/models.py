from django.db import models
from django.utils import timezone

from accounts.models import User


def insurance_choices():
    insurance_set = []
    insurances = User.objects.filter(is_insurance=True)

    for insurance in insurances:
        insurance_set.append(
            (
                str(insurance.username).upper(),
                str(insurance.username).capitalize()
            )
        )
    return insurance_set


class Claim(models.Model):

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    insurance = models.CharField(
        max_length=25,
        choices=insurance_choices(),
        null=False
    )
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user} {self.insurance}'
