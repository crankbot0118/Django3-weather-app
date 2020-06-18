from django.shortcuts import render
import requests 
from .models import City
from .forms import CityForm

# Create your views here.
def home(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=38ce976c51e114d3022e7ea0e64e32c6'
    
    if request.method=='POST':
        form=CityForm(request.POST)
        form.save()

    form=CityForm()
    cities=City.objects.all()
    weather_data=[]
    
    for city in cities:
        r=requests.get(url.format(city)).json()
        city_details={
            'city': city.name,
            'temperature':r['main']['temp'],
            'description' :r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_details)

    print(weather_data)

    return render(request,'weather/home.html',{'city_weather':weather_data,'form':form})
