from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    placa = models.TextField("placa")
    usuario_id = models.TextField("usuario")
    fecha_ingreso = models.TextField("fecha")
    servicio_id = models.TextField("servicio")

    def __str__(self):
        return f'{self.placa}'
