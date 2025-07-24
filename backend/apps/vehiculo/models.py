from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    nombre = models.TextField("nombre", blank=True)
    cedula = models.TextField("cedula", blank=True)
    numero = models.TextField("numero", blank=True)
    placa = models.TextField("placa", null=True)

    def __str__(self):
        return f'{self.placa}'
