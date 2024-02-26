import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import Profile
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.

def index(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'main/profile/index.html', {'profile': profile})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return JsonResponse({'success': 'Your password has changed succesfully. You must log in again'})
        else:
            errors = json.loads(form.errors.as_json())

            formatted_errors = {}
            for field, error_list in errors.items():
                formatted_errors[field] = [error['message'] for error in error_list]
            return JsonResponse({'errors': formatted_errors}, status=400)
    else:
        return JsonResponse({'error': 'Metoda żądania nie jest POST.'}, status=400)