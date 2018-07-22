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
        return HttpResponse(routes)
    
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'home.html', {'form': form})