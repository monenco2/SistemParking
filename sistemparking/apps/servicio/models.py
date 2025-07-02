from django.db import models

# Create your models here.
class Servicio(models.Model):
    servicio = models.TextField("servicio", null=True)

    def __str__(self):
        return f'{self.nombre}'
    