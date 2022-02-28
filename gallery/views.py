from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Image, Location

# Create your views here.
images = []
def index(request):
#I define the function index which will be our view function to display our images.
    global images
    images = Image.objects.all()
    return render(request, 'index.html', {'images':images,})

# I define the function location which will viewing images based on various locations
def location_nairobi(request):
    location_nairobi = Location.objects.get(name='Nairobi')
    images = Image.objects.filter(location=location_nairobi)
    
    return render(request, 'index.html', {'images':images,})

def location_kisumu(request):
    location_kisumu = Location.objects.get(name='Kisumu')
    images = Image.objects.filter(location=location_kisumu)

    return render(request, 'index.html', {'images':images,})

def location_mombasa(request):
    location_mombasa = Location.objects.get(name='Mombasa')
    images = Image.objects.filter(location=location_mombasa)

    return render(request, 'index.html', {'images':images,})

def location_nakuru(request):
    location_nakuru = Location.objects.get(name='Nakuru')
    images = Image.objects.filter(location=location_nakuru)

    return render(request, 'index.html', {'images':images,})

def location_voi(request):
    location_voi = Location.objects.get(name='Voi')
    images = Image.objects.filter(location=location_voi)

    return render(request, 'index.html', {'images':images,})

def location_machakos(request):
    location_machakos = Location.objects.get(name='Machakos')
    images = Image.objects.filter(location=location_machakos)
    
    return render(request, 'index.html', {'images':images,})

def location_taita(request):
    location_taita = Location.objects.get(name='Taita')
    images = Image.objects.filter(location=location_taita)
    
    return render(request, 'index.html', {'images':images,})

def location_meru(request):
    location_meru = Location.objects.get(name='Meru')
    images = Image.objects.filter(location=location_meru)
    
    return render(request, 'index.html', {'images':images,})

def location_garisa(request):
    location_garisa = Location.objects.get(name='Garisa')
    images = Image.objects.filter(location=location_garisa)
    
    return render(request, 'index.html', {'images':images,})

def location_kakamega(request):
    location_kakamega = Location.objects.get(name='Kakamega')
    images = Image.objects.filter(location=location_kakamega)
    
    return render(request, 'index.html', {'images':images,})

def location_malindi(request):
    location_malindi = Location.objects.get(name='Malindi')
    images = Image.objects.filter(location=location_malindi)
    
    return render(request, 'index.html', {'images':images,})

def location_tsavo(request):
    location_tsavo = Location.objects.get(name='Tsavo')
    images = Image.objects.filter(location=location_tsavo)
    
    return render(request, 'index.html', {'images':images,})

def location_nanyuki(request):
    location_nanyuki = Location.objects.get(name='Nanyuki')
    images = Image.objects.filter(location=location_nanyuki)
    
    return render(request, 'index.html', {'images':images,})

def location_nyeri(request):
    location_nyeri = Location.objects.get(name='Nyeri')
    images = Image.objects.filter(location=location_nyeri)
    
    return render(request, 'index.html', {'images':images,})

def search_results(request):

    return render(request)


    
