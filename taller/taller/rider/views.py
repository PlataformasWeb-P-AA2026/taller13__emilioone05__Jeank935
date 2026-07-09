from django.shortcuts import render
from .models import Edificio, Departamento
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# ejemplo de uso django-rest_framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rider.serializers import EdificioSerializer, DepartamentoSerializer


from rider.forms import *


def index(request):
    return render(request, 'rider/index.html')


def edificios_list(request):
    edificios = Edificio.objects.all()
    return render(request, 'rider/edificios.html', {'edificios': edificios})


def departamentos_list(request):
    departamentos = Departamento.objects.select_related('edificio').all()
    return render(request, 'rider/departamentos.html', {'departamentos': departamentos})
