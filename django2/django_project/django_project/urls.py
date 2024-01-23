
from django.contrib import admin
from django.urls import path
from Apps import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dishes/<str:dish>',views.menuitems),
]
