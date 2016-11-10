from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    return HttpResponse("HELLO WORLD DESDE Django")
# Create your views here.
