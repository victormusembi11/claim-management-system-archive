from django.urls import path

from . import views

app_name = 'client'
urlpatterns = [
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('claim/make-claim', views.MakeClaimView.as_view(), name='make-claim'),
]
