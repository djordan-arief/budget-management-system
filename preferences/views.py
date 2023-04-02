from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserPreference
import os
from django.conf import settings
from django.contrib import messages
import json

# Create your views here.

@login_required
def index(request):
    currencies = []
    file = os.path.join(settings.BASE_DIR, 'currencies.json')

    with open(file, 'r') as json_file:
        data = json.load(json_file)
        for key, value in data.items():
            currencies.append({'name': key, 'value': value})

    user_preferences = None
    try:
        user_preferences = UserPreference.objects.get(user=request.user)
    except UserPreference.DoesNotExist:
        pass

    if request.method == 'POST':
        currency = request.POST['currency']
        if user_preferences:
            user_preferences.currency = currency
            user_preferences.save()
        else:
            UserPreference.objects.create(user=request.user, currency=currency)
        messages.success(request, 'Changes saved')

    return render(request, 'preference/index.html', {'currencies': currencies, 'user_preferences': user_preferences})
