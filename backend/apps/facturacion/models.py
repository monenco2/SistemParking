from django.db import models

# Create your models here.here
class Facturacion(models.Model):
    placa = models.TextField("placa", blank=True)
    tiempo = models.TextField("tiempo", blank=True)
    metodo_pago = models.TextField("metodo_pago", null=True)
   
    def __str__(self):
        return f'{self.metodo_pago}'