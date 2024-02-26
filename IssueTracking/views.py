from django.shortcuts import render
import random
import json
from django.shortcuts import redirect
from django.contrib.auth import logout


def index(request):
    return render(request, 'main/index.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def api_logout(request):
    logout(request)
    return redirect('/')
