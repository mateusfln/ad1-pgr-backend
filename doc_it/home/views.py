from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def perguntasfrequentes(request):
    return render(request, 'perguntasfrequentes.html', context={})

def funcionalidades(request):
    return render(request, 'funcionalidades.html')