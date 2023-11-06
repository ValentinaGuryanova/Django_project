from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version

@login_required
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

# @login_required
# @permission_required('catalog.view_product')
def home(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/product.html'


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    success_url = reverse_lazy('catalog:product')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    success_url = reverse_lazy('catalog:product')

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            category=self.kwargs.get('pk'),
        )
        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)
        return queryset

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


class ProductDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('catalog:product')


class VersionListView(LoginRequiredMixin, ListView):
    model = Version
    form_class = VersionForm


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self, *args, **kwargs):
        product_pk = Product.objects.get(pk=self.kwargs.get('pk'))
        return reverse('catalog:view_version', args=[product_pk.pk])