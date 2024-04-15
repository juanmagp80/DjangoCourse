from django.views.generic import ListView
from .models import Product
from django.views.generic.detail import DetailView

class ProductListView(ListView):
    model = Product
    template_name = 'products/product.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    
 