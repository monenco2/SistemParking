from django.db import models

# Create your models here.
class Horaparqueo(models.Model):
    tiempo = models.TextField("tiempo", blank=True)
    lugar = models.TextField("lugar", null=True)
    def __str__(self):
        return f'{self.precio}'