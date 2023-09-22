from django.shortcuts import render
from .models import tare

def home(request):
    tarea= tare.objects.all() 
    return render(request, 'home.html', {'tarea': tarea})