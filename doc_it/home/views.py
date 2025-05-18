from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está em uso.')
        else:
            User.objects.create_user(username=username, email=email, password=password1)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login')

    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def perguntasfrequentes(request):
    return render(request, 'perguntasfrequentes.html', context={})

def funcionalidades(request):
    return render(request, 'funcionalidades.html')