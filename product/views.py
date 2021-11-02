from django.shortcuts import render, get_object_or_404, redirect

from .forms import CreateProductForm
from .models import Category, Product


def home_page(request):
    categories = Category.objects.all()
    return render(request, 'home.html', locals())


def product_list(request, slug):
    products = Product.objects.filter(category__slug=slug)
    # SELECT * FROM Product WHERE category.slug = slug
    return render(request, 'product_list.html', locals())


def product_detail(request, product_id):
    # product = Product.objects.get(id=product_id)
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', locals())


def product_create(request):
    if request.method == 'POST':
        print(request.POST)
        product_form = CreateProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save()
            return redirect('detail', product.id)
    else:
        product_form = CreateProductForm()
    return render(request, 'create_product.html', locals())