from django.urls import path
from . import views

# First we import the path function from the from the django.conf.urls . We then import the app's views module.
# We then create a list named urlpatterns this will be a list of url instances for our app. We then create URL instances by calling the url function.
# We pass in the URL regular expression the view and a name keyword argument.

urlpatterns = [
    path('', views.index, name='index'),
]
