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