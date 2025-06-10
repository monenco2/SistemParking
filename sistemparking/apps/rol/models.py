from django.db import models

# Create your models here.
class Rol (models.Model):
    nombre = models.TextField("nombre")