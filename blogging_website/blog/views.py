from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'blog/index.html', {'title': 'Home'})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact Us'})