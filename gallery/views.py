from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
#I define the function index which will be our view function to display our images.
    global images
    
    return render(request, 'index.html',)