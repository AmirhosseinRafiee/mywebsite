from django.http import HttpResponse
from django.shortcuts import render

def index_view(request):
    return HttpResponse('<h1>salam</h1>')

def contact_view(request):
    return HttpResponse('<h1>contact</h1>')

def services_view(request):
    return HttpResponse('<h1>services</h1>')

