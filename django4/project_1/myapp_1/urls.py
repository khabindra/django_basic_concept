from django.urls import path
from myapp_1.views import create_blog_post



urlpatterns = {
    path('home/',create_blog_post,name='create_blog_post')
}