from django.forms.models import ModelForm

from .models import Claim


class ClaimForm(ModelForm):

    class Meta:
        model = Claim
        fields = (
            'client',
            'insurance',
            'title',
            'description'
        )
