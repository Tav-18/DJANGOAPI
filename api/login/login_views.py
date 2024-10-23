from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# view login

def login_views(request):
    template_name = "login.html"
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'That is not precious.')
    return render(request, template_name)

# register views
def register_views(request):
    template_name = "registration.html"
    
    return render(request, template_name)

# forgot views
def forgot_views(request):
    template_name = "forgot.html"
    
    return render(request, template_name)

# logout view
def logout_views(request):
    logout(request)
    return redirect('login')
