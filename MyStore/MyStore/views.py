from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("<h1> Welcome to Django Project: Home page </h1>")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("<h1> Welcome to Django Project: About page </h1>")

def about(request):
    return HttpResponse("<h1> Welcome to Django Project: Contact page </h1>")