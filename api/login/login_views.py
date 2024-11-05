from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



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
    template_name = "register.html"
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        
        # Validación de contraseñas
        if password != password_confirmation:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, template_name)
        
        # Validación de existencia de usuario
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
            return render(request, template_name)
        
        # Validación de existencia de correo electrónico
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya existe')
            return render(request, template_name)
        
        # Creación de usuario
        user = User(
            username=username,
            email=email,
            password=make_password(password)
        )
        user.save()
        messages.success(request, 'Usuario creado exitosamente')
        
        # Redireccionar a la página de login después de un registro exitoso
        return redirect('login')
    
    return render(request, template_name)






# forgot views
def forgot_views(request):
    template_name = "forgot.html"
    
    return render(request, template_name)

# logout view
def logout_views(request):
    logout(request)
    return redirect('login')
