from django.db import models
from django.core.exceptions import ValidationError

# Validación 1: Precio
def validar_precio(value):
    if value < 0:
        raise ValidationError("El precio no puede ser negativo.")

# Validación 2: Nombre vacío o muy corto
def validar_nombre_largo(value):
    if len(value) < 3:
        raise ValidationError("El nombre debe tener al menos 3 caracteres.")

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100, validators=[validar_nombre_largo])
    direccion = models.CharField(max_length=200)

    def __str__(selt):
        return selt.nombre

class Repartidor(models.Model):
    nombre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)

class Producto(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_precio])

class Pedido(models.Model):
    cliente = models.CharField(max_length=100)
    productos = models.ManyToManyField(Producto)
    repartidor = models.ForeignKey(Repartidor, on_delete=models.SET_NULL, null=True)
    completado = models.BooleanField(default=False)
