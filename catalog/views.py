from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, CreateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


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


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        for product in context['object_list']:
            active_version = product.version_set.filter(is_current_version=True).first()
            if active_version:
                product.active_version_number = active_version.version_number
                product.active_version_name = active_version.version_name
            else:
                product.active_version_number = None
                product.active_version_name = None


    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
    #     if self.request.method == "POST":
    #         context_data['formset'] = VersionFormset(self.request.POST)
    #     else:
    #         context_data['formset'] = VersionFormset()
    #     return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class VersionListView(ListView):
    model = Version
    form_class = VersionForm


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self, *args, **kwargs):
        product_pk = Product.objects.get(pk=self.kwargs.get('pk'))
        return reverse('catalog:view_version', args=[product_pk.pk])