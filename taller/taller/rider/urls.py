
"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path, include
# se importa las vistas de la aplicación
from rider import views
from rest_framework import routers
# Estos viewset estan conctaods a los serializers que los serializers estan al modelo
router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'edificios', views.EdificioViewSet)
router.register(r'departamentos', views.DepartamentoViewSet)
# app_name = 'rider'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('edificios/', views.edificios_list, name='edificios_list'),
    path('departamentos/', views.departamentos_list, name='departamentos_list'),
]


