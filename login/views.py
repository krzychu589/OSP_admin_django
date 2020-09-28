from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login\\../register/templates/registration/login.html')

def password(request):
    return render(request, 'login\\password.html')

