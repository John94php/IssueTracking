from django.shortcuts import render
import random
import json
from django.shortcuts import redirect
from django.contrib.auth import logout

def index(request):
    names = ("bob", "dan", "jack", "lizzy", "susan")

    items = []
    for i in range(100):
        items.append({
            "name": random.choice(names),
            "age": random.randint(20, 80),
            "url": "https://example.com",
        })

    context = {}
    context["items_json"] = json.dumps(items)

    return render(request, 'index.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')
