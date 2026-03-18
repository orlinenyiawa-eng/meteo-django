from django.shortcuts import render
import requests
from django.shortcuts import render

def home(request):
    context = {
        'city': 'Bafoussam',
        'temperature': 25,
        'description': 'Ensoleillé'
    }
    return render(request, 'meteo/home.html', context)
def dashboard(request):
    return render(request, 'meteo/dashboard.html')
