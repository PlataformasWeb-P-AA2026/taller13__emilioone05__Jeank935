from django.shortcuts import render
from .models import Edificio, Departamento


def index(request):
    return render(request, 'rider/index.html')


def edificios_list(request):
    edificios = Edificio.objects.all()
    return render(request, 'rider/edificios.html', {'edificios': edificios})


def departamentos_list(request):
    departamentos = Departamento.objects.select_related('edificio').all()
    return render(request, 'rider/departamentos.html', {'departamentos': departamentos})