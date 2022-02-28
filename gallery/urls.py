from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# First we import the path function from the from the django.conf.urls . We then import the app's views module.
# We then create a list named urlpatterns this will be a list of url instances for our app. We then create URL instances by calling the url function.
# We pass in the URL regular expression the view and a name keyword argument.

urlpatterns = [
    path('', views.index, name='index'),
    path('nairobi/', views.location_nairobi, name='location_nairobi'),
    path('kisumu/', views.location_kisumu, name='location_kisumu'),
    path('mombasa/', views.location_mombasa, name='location_mombasa'),
    path('nakuru/', views.location_nakuru, name='location_nakuru'),
    path('voi/', views.location_voi, name='location_voi'),
    path('machakos/', views.location_machakos, name='location_machakos'),
    path('taita/', views.location_taita, name='location_taita'),
    path('meru/', views.location_meru, name='location_meru'),
    path('garisa/', views.location_garisa, name='location_garisa'),
    path('kakamega/', views.location_kakamega, name='location_kakamega'),
    path('malindi/', views.location_malindi, name='location_malindi'),
    path('tsavo/', views.location_tsavo, name='location_tsavo'),
    path('nanyuki/', views.location_nanyuki, name='location_nanyuki'),
    path('nyeri/', views.location_nyeri, name='location_nyeri'), 
    path('search/', views.search_results, name='search_results'), 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

