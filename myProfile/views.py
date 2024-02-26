import json
import time

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.

def index(request):
    try:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'main/profile/index.html', {'profile': profile})
    except Exception as e:
        logout(request)
        return redirect('/')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            message = 'Your password has changed successfully. You will be logged out in a few seconds.'
            response_data = {'success': message}

            return JsonResponse(response_data)

        else:
            errors = json.loads(form.errors.as_json())

            formatted_errors = {}
            for field, error_list in errors.items():
                formatted_errors[field] = [error['message'] for error in error_list]
            return JsonResponse({'errors': formatted_errors}, status=400)
    else:
        return JsonResponse({'error': 'Metoda żądania nie jest POST.'}, status=400)