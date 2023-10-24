from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from catalog.models import Product


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def home(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description',)
    success_url = reverse_lazy('product:list')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description',)
    success_url = reverse_lazy('product:list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:list')