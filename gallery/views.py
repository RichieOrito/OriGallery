from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
images = []
def index(request):
#I define the function index which will be our view function to display our images.
    global images
    
    return render(request, 'index.html', {'images':images,})

# I define the function location which will viewing images based on various locations
def location_nairobi(request):
    return render(request, 'index.html', {'images':images,})

def location_kisumu(request):
    
    return render(request, 'index.html', {'images':images,})

def location_mombasa(request):
    
    return render(request, 'index.html', {'images':images,})

def location_nakuru(request):
    
    return render(request, 'index.html', {'images':images,})

def location_voi(request):
    
    return render(request, 'index.html', {'images':images,})

def location_machakos(request):
    
    return render(request, 'index.html', {'images':images,})

def location_taita(request):
    
    return render(request, 'index.html', {'images':images,})

def location_meru(request):
    
    return render(request, 'index.html', {'images':images,})

def location_garisa(request):
    
    return render(request, 'index.html', {'images':images,})

def location_kakamega(request):
    
    return render(request, 'index.html', {'images':images,})

def location_malindi(request):
    
    return render(request, 'index.html', {'images':images,})

def location_tsavo(request):
    
    return render(request, 'index.html', {'images':images,})

def location_nanyuki(request):
    
    return render(request, 'index.html', {'images':images,})

def location_nyeri(request):
    
    return render(request, 'index.html', {'images':images,})

def search_results(request):

    return render(request, 'index.html',)


    
