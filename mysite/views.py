from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user )
            return redirect('index')

        print(username)
        print(password)

    
    
    return render(request, 'users/login.html', {
        'message': 'Iniciar sesión'
    })

    
    

