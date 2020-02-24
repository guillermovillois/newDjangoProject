from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    my_title = 'Hello world!'
    context = {'title':my_title}
    return render(request, 'home.html', context )

def about_page(request):
    return render(request, 'contact.html',{'title':'About'})

def contact_page(request):
    return render(request, 'hello_world.html',{'title':'Contact'})