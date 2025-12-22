from django.shortcuts import render, redirect
from .forms import ProductForm
from.models import Product
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ProductForm()
    return render(request, 'create.html', {'form': form})
def product_read(request):
    product_list=Product.objects.all()
    return render(request,'retrieve.html',{'product_list':product_list})