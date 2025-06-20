from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'ProductHub/home.html', { 'products': products })

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'ProductHub/details.html', { 'product': product })