from django.urls import path
from . import views

app_name = 'rider'

urlpatterns = [
    path('', views.index, name='index'),
    path('edificios/', views.edificios_list, name='edificios_list'),
    path('departamentos/', views.departamentos_list, name='departamentos_list'),
]