from django.urls import path
from Apps.views import *

app_name = 'Apps'

urlpatterns = [
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('menu/',menu,name='menu'),
    path('book',book,name='book'),
]