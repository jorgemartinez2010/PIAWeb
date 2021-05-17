from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=60)
    presentacion = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return self.descripcion

class Proveedor(models.Model):
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Estante(models.Model):
    clave = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Locker(models.Model):
    clave = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Mueble(models.Model):
    clave = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Caja(models.Model):
    clave = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre