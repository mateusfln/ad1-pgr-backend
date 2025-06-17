from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import viewsets
from .models import UserProfile, Category, Document, DocumentLog, Attachment
from .serializers import UserProfileSerializer, CategorySerializer, DocumentSerializer, DocumentLogSerializer, AttachmentSerializer
# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já está em uso.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está em uso.')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # faz o login
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('login')

def perguntasfrequentes(request):
    return render(request, 'perguntasfrequentes.html', context={})

def funcionalidades(request):
    return render(request, 'funcionalidades.html')



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentLogViewSet(viewsets.ModelViewSet):
    queryset = DocumentLog.objects.all()
    serializer_class = DocumentLogSerializer

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
