from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error = 'Invalid credentials'
            return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'login.html')
from django.contrib.auth.decorators import login_required

@login_required
def index_view(request):
    return render(request, 'index.html', {'user': request.user})
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')