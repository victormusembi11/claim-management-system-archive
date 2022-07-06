from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import InsuranceSignUpForm
from ..models import User


class InsuranceSignUpView(CreateView):

    model = User
    form_class = InsuranceSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'insurance'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return redirect('accounts:login')
