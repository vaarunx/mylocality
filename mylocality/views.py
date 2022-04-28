from django.shortcuts import render
import requests
from django.conf import settings
import what3words
import geocoder




# Create your views here.
def home(request):
    
    return render(request , 'base.html')

def test(request):


    context =[

    ]

    return render(request, 'testing.html')



    

def mappingPlaces(request):
    g = geocoder.ip('me')
    print(g.latlng)
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=13.02537533546862+80.26086994528788&radius=1500&type=restaurant&key={settings.GOOGLE_KEY}"
    response = requests.get(url)
    data = response.json()
    results = data['results']
    place_id = results[0]['place_id']    
    place_id_list = []
    #geocoder = what3words.Geocoder('YB59FL4H')
    #res = geocoder.convert_to_3wa(what3words.Coordinates(13.0096034, 80.0051176)).get('words')
    for i in range(len(results)):
        place_id = {"placeId":results[i]['place_id']}
        place_id_list.append(place_id)
        print(place_id)
    print(place_id_list)

    context = {
        'place_id_list' : place_id_list
    }
    return render(request , 'index.html',context)

# def search_maps(request):
#     return




