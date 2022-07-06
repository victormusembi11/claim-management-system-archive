from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .decorators import insurance_required


@login_required
@insurance_required
def dashboard_view(request):

    return render(request, 'insurance/dashboard.html', {
        'message': f'Hello {request.user.username}'
    })
