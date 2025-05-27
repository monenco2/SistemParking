from django.db import models

# Create your models here.here
class Facturacion(models.model):
    metodo_pago = models.TextField("pago")
    vehiculo_id = models.TextField("vehiculo")
    valor_pagar = models.TextField("valor")