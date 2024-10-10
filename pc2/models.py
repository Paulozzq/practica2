from django.db import models

# models.py
from django.db import models

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'marca'  
        managed = False   

class Modelo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    class Meta:
        db_table = 'modelo'
        managed = False

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    stock = models.IntegerField()
    activo = models.BooleanField(default=True)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'productos' 
        managed = False

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)  # Campo de nombre de usuario
    password = models.CharField(max_length=255)  # Campo de contraseña (recomendado almacenar hashes)

    def __str__(self):
        return self.username 