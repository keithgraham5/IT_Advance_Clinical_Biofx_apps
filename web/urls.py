from django.urls import path
from . import views

urlpatterns = [
    path('', views.variant_list, name='variant_list'),
    path('search/', views.searchpage, name='search_result'),
]
