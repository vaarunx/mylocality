from django.shortcuts import render
import requests
from django.conf import settings


# Create your views here.
def home(request):
    
    return render(request , 'base.html')

def test(request):


    context =[

    ]

    return render(request, 'testing.html')


def mappingPlaces(request):
    
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=13.0096034+80.0051176&radius=1500&type=restaurant&keyword=cruise&key={settings.GOOGLE_KEY}"
    response = requests.get(url)
    data = response.json()
    results = data['results']
    print("Hello")
    print(results[0]['place_id'])

    #print(data)
    return render(request, 'testing.html')



