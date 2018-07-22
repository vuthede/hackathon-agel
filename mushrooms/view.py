from django.db import models
from src.routing import single_source_routing
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render
from .forms import NameForm
import datetime
from django.http import HttpResponse
import src.globals
import src.routemanager 
import requests
from django.http import JsonResponse
import json
import urllib.request
import nexmo
# def helloworld(request):
#     print("this is request ahi ")
#     print("hello world")
#     return "hello world"

class RoutingList():
    
    def current_datetime(request):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        print(RouteManager.numberOfDustbins())
        return HttpResponse(html)

    def pointre(request):
        points = [(10.775979, 106.647416), (10.778877, 106.645034), (10.778998, 106.646461), (10.778280, 106.647274),
            (10.778584, 106.649881), (10.779987, 106.650601), (10.779507, 106.649450), (10.779073, 106.650368)]
        numTrucks = 3
        routes = single_source_routing(points = points, numTrucks = numTrucks)
        print(routes)
        html = "<html><body>It is working!!! Haha %s.</body></html>" 
        return HttpResponse(routes)
    
def load_color(request):
    latTL = request.POST.get('latTL')
    lonTL = request.POST.get('lonTL')
    latTR = request.POST.get('latTR')
    lonTR = request.POST.get('lonTR')
    latBL = request.POST.get('latBL')
    lonBL = request.POST.get('lonBL')
    latBR = request.POST.get('latBR')
    lonBR = request.POST.get('lonBR')
    zoom = request.POST.get('zoom')
    print(latTL)
    url = 'https://traffic.hcmut.edu.vn/hcm/rest/tc/init?latTL=' + latTL + '&lonTL=' + lonTL + '&latTR=' + latTR + '&lonTR=' + lonTR + '&latBL=' + latBL + '&lonBL=' + lonBL + '&latBR=' + latBR + '&lonBR=' + lonBR + '&zoom=' + zoom

#    url = 'https://traffic.hcmut.edu.vn'+request
    r = requests.get(url, params=request.GET)
    print(r.json())
    print(type(r.json()))
    data = r.json()
    last = data['last']
    key = None
    while not last:
        key = data['key']
        contents = urllib.request.urlopen("https://traffic.hcmut.edu.vn/hcm/rest/tc/get?key="+str(key)).read().decode("utf8")
        res = json.loads(contents)
        data["segs"] = data["segs"] + res["segs"]
        last = res["last"]
        data["key"] = res.get("key", None)
    return JsonResponse(data)
def get_distance(request):
    distance = float(request.POST.get('distance'))
    print(distance)
    time = distance / 30 *60
    print(time)
    if time <= 5:
        client = nexmo.Client(
            application_id='81980ab0-cf63-44c1-9a2c-4f0169a45e08',
            private_key='C:\\Users\\ASUS\\Documents\\hackathon-agel\\mushrooms\\private.key'
        )

        to_number = [{'type': 'phone', 'number': '84968399590'}]
        from_number = {'type': 'phone', 'number': '841646905917'}
        answer_url = ['https://api.myjson.com/bins/1bkt7e']

        response = client.create_call({
            'to': to_number,
            'from': from_number,
            'answer_url': answer_url
        })
    elif time <=10:
        client = nexmo.Client(key='907b6963', secret='RgznGXxoeojL49gh')
        response = client.send_message(
        {
        'from': 'Python',
        'to': '84968399590', 'text': 'You will receive your packet in 10 minute'
        })
        print('aaaa')
    return 0