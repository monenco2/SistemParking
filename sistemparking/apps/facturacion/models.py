from django.db import models

# Create your models here.here
class Facturacion(models.Model):
    metodo_pago = models.TextField("pago")
    vehiculo_id = models.TextField("vehiculo")
    valor_pagar = models.TextField("valor")

    def __str__(self):
        return f'{self.metodo_pago}'