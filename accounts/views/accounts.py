from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from ..models import User


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    model = User
    template_name = 'accounts/accounts.html'
    login_url = reverse_lazy('accounts:login')

    permission_required = [
        'can_view_user'
    ]


class UserDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):

    model = User
    template_name = 'accounts/account.html'
    login_url = reverse_lazy('accounts:login')

    permission_required = [
        'can_view_user'
    ]


class RegisterOptionView(TemplateView):

    template_name = 'accounts/register-options.html'
