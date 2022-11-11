from django.urls import path
from . import views

urlpatterns = [
    path('', views.variant_list, name='variant_list'),
    path('filter', views.search, name='filter'),
    path('search/', views.searchpage, name='search_result'),
]

