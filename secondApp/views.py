from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def adios(response):
    return HttpResponse("<h2>ADIOSITO</h2>")
def displayDateTime(request):
    dt=datetime.now()
    s="<h2><b>La Hora es:  </b>"+str(dt)+"</h2>"
    return HttpResponse(s)
