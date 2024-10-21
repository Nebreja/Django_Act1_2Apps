from django.shortcuts import render

def home(request):
    return render(request, 'app2/home.html')
def signup(request):
    if request.method == 'POST':
        # Handle signup logic here
        pass
    return render(request, 'app2/signup.html')

def signin(request):
    if request.method == 'POST':
        # Handle signin logic here
        pass
    return render(request, 'app2/signin.html')