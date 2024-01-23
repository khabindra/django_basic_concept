from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def menuitems(request,dish):
    items ={
        'pasta':'pasta is a type of noodle made from combination of ......',
        'tea':'tea is combination of water ,sugar, and other.',
        'meat':'it is best non-veg foods.'
    }
    description = items[dish]
    response = f'<h2>{dish} </h2>'+ description
    return HttpResponse(response)

# http://127.0.0.1:8000/dishes/meat
# http://127.0.0.1:8000/dishes/pasta
# http://127.0.0.1:8000/dishes/tea
# try above commented after running the server 