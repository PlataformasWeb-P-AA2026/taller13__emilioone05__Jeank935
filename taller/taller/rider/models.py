from django.db import models


class Edificio(models.Model):
    RESIDENCIAL = "residencial"
    COMERCIAL = "comercial"

    TIPOS_EDIFICIO = [
        (RESIDENCIAL, "Residencial"),
        (COMERCIAL, "Comercial"),
    ]

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS_EDIFICIO)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
        self.direccion,
        self.ciudad,
        self.tipo,
        )
       
class Departamento(models.Model):
    nombre_completo_propietario = models.CharField(max_length=150)
    costo_departamento = models.DecimalField(max_digits=12, decimal_places=2)
    numero_cuartos = models.IntegerField()
    edificio = models.ForeignKey(
        Edificio,
        on_delete=models.CASCADE,
        related_name="departamentos",
    )

    def __str__(self):
        return "%s %s %s" % (
            self.nombre_completo_propietario,
            self.costo_departamento,
            self.numero_cuartos,
        )
