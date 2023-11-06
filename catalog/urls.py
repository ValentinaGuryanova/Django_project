from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, ProductListView, ProductCreateView, ProductUpdateView, VersionListView, \
    ProductDelete
app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/', ProductListView.as_view(), name='product'),
    path('create', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('', VersionListView.as_view(), name='list'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='delete_product'),
]
