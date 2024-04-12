from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegisterForm
from django.contrib.auth.models import User
def index(request):
    return render (request, 'index.html', {'message': 'Listado de productos', 'title': 'Productos', 'products': [
        {'name': 'Camiseta', 'price': 50, 'Stock': True},
        {'name': 'Pantalón', 'price': 100, 'Stock': False},
        {'name': 'Zapatos', 'price': 200, 'Stock': True},
        {'name': 'Gorra', 'price': 20, 'Stock': False},
        {'name': 'Zapatos', 'price': 200, 'Stock': True},
        {'name': 'Gorra', 'price': 20, 'Stock': False},
    ]
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user )
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')

        print(username)
        print(password)

    
    
    return render(request, 'users/login.html', {
        'message': 'Iniciar sesión'
    })


def logout_view(request):
        
        logout(request)
        messages.success(request, 'Sesión cerrada exitosamente')
        return redirect('login')

       
        


def register (request):
    if request.user.is_authenticated:
        return redirect('index')
    
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password)
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')
        else:
            messages.error(request, 'Ocurrió un error al crear el usuario')
        
        print(username)
        print(email)
        print(password)
    
    return render(request, 'users/register.html', {
        'form': form,
        'message': 'Registro de usuario'
    })
    


    
    
    

