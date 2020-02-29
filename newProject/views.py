from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    my_title = 'Hello world!'
    context = {'title':my_title}
    return render(request, 'home.html', context )

def about_page(request):
    return render(request, 'contact.html',{'title':'About'})

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {'title':'Contact','form': form}
    return render(request, 'form.html', context)