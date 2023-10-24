from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name


urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/', ProductListView.as_view(), name='product'),
    path('create', ProductCreateView.as_view(), name='create'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete')
]
