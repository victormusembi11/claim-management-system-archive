from django.urls import path, include

from .views.insurance import InsuranceSignUpView
from .views.client import ClientSignUpView
from .views.accounts import RegisterOptionView, UserListView, UserDetailView


app_name = 'accounts'
urlpatterns = [
    path('login', include('django.contrib.auth.urls'), name='login'),
    path(
        'register-options',
        RegisterOptionView.as_view(),
        name='register-options'
    ),
    path('signup/insurance', InsuranceSignUpView.as_view(), name='insurance'),
    path('signup/client', ClientSignUpView.as_view(), name='client'),
    path('list', UserListView.as_view(), name='all-accounts'),
    path('detail/<int:pk>', UserDetailView.as_view(), name='user-account'),
]
