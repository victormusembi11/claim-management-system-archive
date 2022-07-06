from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import ClientSignUpForm
from ..models import User


class ClientSignUpView(CreateView):

    model = User
    form_class = ClientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return redirect('accounts:login')
