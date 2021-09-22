from django.shortcuts import render
import json
import urllib.request
import logging
import string

# Create your views here.
def index(request):
    if request.method == 'POST':
        location = request.POST['location']
        
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=5f74f3cd56b247c2233db0030cf92019').read()
        json_data = json.loads(res)

        logger = logging.getLogger(__name__)
        # logger.error(json_data['weather'][0]['main'])

        data = {
            "country": str(json_data['sys']['country']),
            "longitude": str(json_data['coord']['lon']),
            "latitude": str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "weather": string.capwords(str(json_data['weather'][0]['main'])),
            "type": string.capwords(str(json_data['weather'][0]['description'])),
            "wind_speed": str(json_data['wind']['speed']) + 'mph',
        }

        location = string.capwords(location)

        return render(request, 'index.html', {'location': location, 'data': data})

    else:
        return render(request, 'index.html')
