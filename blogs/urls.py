from django.urls import path, include

import blogs
from blogs.apps import BlogsConfig
from blogs.views import BlogsCreateView, BlogsListView, BlogsDetailView, BlogsUpdateView, BlogsDeleteView
from catalog.views import contacts, home

app_name = BlogsConfig.name


urlpatterns = [
    path('create', BlogsCreateView.as_view(), name='create'),
    path('', BlogsListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogsDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogsUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogsDeleteView.as_view(), name='delete'),
]