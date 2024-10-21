from django.shortcuts import render, redirect

def home(request):
    return render(request, 'app1/home.html')

def signup(request):
    if request.method == 'POST':
        # Handle signup logic here
        pass
    return render(request, 'app1/signup.html')

def signin(request):
    if request.method == 'POST':
        # Handle signin logic here
        pass
    return render(request, 'app1/signin.html')
