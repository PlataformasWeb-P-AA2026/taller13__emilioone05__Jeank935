from django.contrib import admin


from rider.models import Edificio, Departamento
class EdificioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad','tipo')
    search_fields = ('nombre', 'direccion')

admin.site.register(Edificio, EdificioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo_propietario', 'costo_departamento', 'numero_cuartos','edificio')
    search_fields = ('nombre_completo_propietario', 'numero_cuartos')

admin.site.register(Departamento, DepartamentoAdmin)