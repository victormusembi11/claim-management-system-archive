from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from accounts.models import User


class InsuranceSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_insurance = True
        if commit:
            user.save()
        return user


class ClientSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        if commit:
            user.save()
        return user
