from django.http import HttpResponse
from django.shortcuts import render

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

    

