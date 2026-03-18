from django.shortcuts import render
import requests
from django.shortcuts import render

def home(request):
    city = request.GET.get('city', 'Bafoussam')
    api_key = 'TON_API_KEY'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    context = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
    }

    return render(request, 'meteo/home.html', context)
# Create your views here.
