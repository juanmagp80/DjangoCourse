from . import views
from django.contrib import admin
from django.urls import path
from django.urls import include
from products.views import ProductListView


urlpatterns = [

    path('', ProductListView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('usuarios/login', views.login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),

    path('usuarios/registro', views.register, name='register'),
    path('productos/', include('products.urls')),

]
