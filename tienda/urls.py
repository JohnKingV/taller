from django.urls import path
from . import views

urlpatterns =[
    path('index', views.index, name='index'),
    path('compras', views.compras, name='compras'),
    path('registro', views.registro, name='registro'),
]