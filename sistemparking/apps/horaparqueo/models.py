from django.db import models

# Create your models here.
class Horaparqueo(models.Model):
    precio = models.TextField("precio")
    servicio_id = models.TextField("servicio")

    def __str__(self):
        return f'{self.precio}'