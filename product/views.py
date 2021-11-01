from django.shortcuts import render
from .models import Category, Product

def home_page(request):
    categories = Category.objects.all()
    return render(request, 'home.html', locals())

def product_list(request, slug):
    products = Product.objects.filter(category__slug=slug)
    # SELECT * FROM Product WHERE category.slug = slug
    return render(request, 'product_list.html', locals())