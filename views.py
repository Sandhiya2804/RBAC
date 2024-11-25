# authentication/views.py
from django.shortcuts import render

def login_view(request):
    # Your login logic here
    return render(request, 'authentication/login.html')

def signup_view(request):
    # Your signup logic here
    return render(request, 'authentication/signup.html')
