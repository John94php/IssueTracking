import json
import time

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Profile, Settings
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import activate


# Create your views here.

def index(request):
    try:
        profile = Profile.objects.get(user=request.user)
        settings = Settings.objects.get(user=request.user)
        return render(request, 'main/profile/index.html', {'profile': profile,"settings": settings})
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


def change_language(request, language_code):
    activate(language_code)
    return redirect(request.META.get('HTTP_REFERER'))


def user_notifications(request):
    user_id = request.user.id
    try:
        obj = Settings.objects.get(user_id=user_id)
    except Settings.DoesNotExist:
        obj = Settings.objects.create(user_id=user_id, app_notifications=0, mail_notifications=0, dark_mode=0)

    app_notifications = request.GET.get('app_notifications')
    mail_notifications = request.GET.get('mail_notifications')
    print(app_notifications)
    output = ""

    if app_notifications == "1":
        output = "Wybrano powiadomienia w aplikacji."
        obj.app_notifications = 1
    elif app_notifications == "0":
        output = "Odznaczono powiadomienia w aplikacji."
        obj.app_notifications = 0

    if mail_notifications == "1":
        output = "Wybrano powiadomienia mailowe."
        obj.mail_notifications = 1
    elif mail_notifications == "0":
        output = "Odznaczono powiadomienia mailowe."
        obj.mail_notifications = 0

    # Zawsze ustaw dark_mode na 0
    obj.dark_mode = 0
    obj.save()

    return JsonResponse(output, safe=False)