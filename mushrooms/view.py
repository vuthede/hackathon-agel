from django.db import models
from src.routing import single_source_routing
from src.routing import multiple_source_routing
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
import ast
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
       ##print(routes)
        html = "<html><body>It is working!!! Haha %s.</body></html>"
        print(routes)
        return HttpResponse(routes)
    

    def pointre_multi(request):
        points = [(10.775979, 106.647416), (10.778877, 106.645034), (10.778998, 106.646461), (10.778280, 106.647274),
            (10.778584, 106.649881), (10.779987, 106.650601), (10.779507, 106.649450), (10.779073, 106.650368)]
        points0 = [(10.761901, 106.673298), (10.757931, 106.677504), (10.752695, 106.677504), (10.751428, 106.66995), (10.754553, 106.662226), (10.762745, 106.665487), (10.764097, 106.653471), (10.770177, 106.668577), (10.770515, 106.689091), (10.749907, 106.698189), (10.746276, 106.684713), (10.764941, 106.697245), (10.756495, 106.711836), (10.783948, 106.679134), (10.740706, 106.677418), (10.738341, 106.662827), (10.744254, 106.70248), (10.778375, 106.66008)]
        
        points1 = [(10.755216, 106.631927), (10.751838, 106.643429), (10.745419, 106.638966), (10.74829, 106.624374), (10.770081, 106.625748), (10.767716, 106.685314), (10.749979, 106.661968), (10.73731, 106.653214), (10.738999, 106.626263), (10.73731, 106.61253), (10.767716, 106.59708), (10.785113, 106.621628), (10.79018, 106.639309), (10.778357, 106.674328), (10.767209, 106.650982), (10.734776, 106.615963), (10.738999, 106.674328), (10.735959, 106.705399), (10.748797, 106.727886)]


        points2 = [(10.780103, 106.680765), (10.788464, 106.682568), (10.788717, 106.671238), (10.782637, 106.678877), (10.777992, 106.677504), (10.780103, 106.685658), (10.776725, 106.682653), (10.772164, 106.678877), (10.776556, 106.668062), (10.780525, 106.689005), (10.77284, 106.688919), (10.767688, 106.6854), (10.786944, 106.687117), (10.78745, 106.705227), (10.773093, 106.696386), (10.768533, 106.689692), (10.769546, 106.658535), (10.783988, 106.662054)]
        
        points3 = [(10.773782, 106.697502), (10.768547, 106.696386), (10.768294, 106.704197), (10.765675, 106.704154), (10.767956, 106.687074), (10.776317, 106.685314), (10.779399, 106.698103), (10.774205, 106.677418), (10.768716, 106.671968), (10.793838, 106.686859), (10.739343, 106.691151), (10.755222, 106.6745), (10.757249, 106.652699), (10.747114, 106.696644), (10.76333, 106.675358), (10.77735, 106.631927), (10.766877, 106.638794), (10.774309, 106.656132)]
        
        

        routes = multiple_source_routing([points, points0],  max_num_trucks=2)
        html = "<html><body>It is working!!! Haha %s.</body></html>" 

        routes = ast.literal_eval(routes)
        routes = map(lambda i:i[:1],routes)
        print(routes)
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
    # print(r.json())
    # print(type(r.json()))
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