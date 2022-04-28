from django.shortcuts import render
import requests
from django.conf import settings
import what3words



# Create your views here.
def home(request):
    
    return render(request , 'base.html')

def test(request):


    context =[

    ]

    return render(request, 'testing.html')


def random(request):
    
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=13.02537533546862+80.26086994528788&radius=1500&type=restaurant&key={settings.GOOGLE_KEY}"
    response = requests.get(url)
    data = response.json()
    results = data['results']
    place_id = results[0]['place_id']    
    geocoder = what3words.Geocoder('YB59FL4H')
    res = geocoder.convert_to_3wa(what3words.Coordinates(13.0096034, 80.0051176)).get('words')
    print(place_id)
    print(res)
    return render(request, 'testing.html')
    

def mappingPlaces(request):
    return render(request , 'index.html')




