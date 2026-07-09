from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from rider.models import Edificio, Departamento

class EdificioteForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese direccion por favor'),
            'ciudad': _('Ingrese ciudad por favor'),
            'tipo': _('Ingrese tipo por favor'),
        }


    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())
        """
        valor = "René"
        ["René"] # 1
        len( ["René"])
        """

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos nombre por favor")
        return valor

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_completo_propietario', 'costo_departamento', 'numero_cuartos','edificio']

