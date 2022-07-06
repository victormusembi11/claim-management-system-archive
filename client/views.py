from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .decorators import client_required
from .forms import ClaimForm


@login_required
@client_required
def dashboard_view(request):

    return render(request, 'client/dashboard.html', {
        'message': f'Hello {request.user.first_name}'
    })


class MakeClaimView(LoginRequiredMixin, CreateView):

    form_class = ClaimForm
    template_name = 'client/make-claim.html'
    success_url = reverse_lazy('client:dashboard')
