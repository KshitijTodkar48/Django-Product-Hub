from django.shortcuts import render
from .models import Product, Seller
from django.shortcuts import get_object_or_404
from .forms import ProductForm

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'ProductHub/home.html', { 'products': products })

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'ProductHub/details.html', { 'product': product })

def product_sellers(request):
    sellers = None

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            product = form.cleaned_data['product']
            sellers = Seller.objects.filter(products = product)
    else:
        form = ProductForm()

    return render(request, 'ProductHub/sellers.html', { 'sellers': sellers, 'form': form })