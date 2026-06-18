from django.shortcuts import render
import requests

def home(request):
    weather_data = None
    error = None
    
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'YOUR_API_KEY_HERE'  # Replace with your OpenWeatherMap API key from openweathermap.org
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        try:
            response = requests.get(url)
            data = response.json()
            
            if data['cod'] == 200:
                weather_data = {
                    'city': data['name'],
                    'country': data['sys']['country'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                    'humidity': data['main']['humidity'],
                    'wind_speed': data['wind']['speed'],
                }
            else:
                error = data.get('message', 'City not found')
        except:
            error = 'Error fetching weather data. Please check API key.'
    
    return render(request, 'weather/home.html', {'weather_data': weather_data, 'error': error})