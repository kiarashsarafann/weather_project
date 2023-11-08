from django.shortcuts import render
import requests
from django.http import JsonResponse
import datetime
from home_module.forms import SearchForm


def weather(request, city):
    api_key = '0684464095cb047b32216bdb32797a4e'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)


def index_page(request):
    search_form = SearchForm
    if request.method == 'POST':
        city = str(request.POST.get('city'))
        api_key = '0684464095cb047b32216bdb32797a4e'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        data = requests.get(url).json()

        date_now = datetime.datetime.now()
        week_day = date_now.strftime('%A')
        month_name = date_now.strftime('%b')
        month_day = date_now.strftime('%d')

        temp = int(data['main']['temp'])
        city_name = data['name']
        wind_speed = data['wind']['speed']
        wind_degree = data['wind']['deg']
        weather_status = data['weather'][0]['main']
        rain = '0'

        if 'rain' in data:
            rain = data['rain']['1h']

        context = {
            'search_form': search_form,
            'city_name': city_name,
            'temp': temp,
            'wind_speed': wind_speed,
            'week_day': week_day,
            'month_name': month_name,
            'month_day': month_day,
            'rain': rain,
            'wind_degree': wind_degree,
            'weather_status': weather_status,
        }
        return render(request, 'home_module/index.html', context)
    else:
        return render(request, 'home_module/index.html', {'search_form': search_form})
