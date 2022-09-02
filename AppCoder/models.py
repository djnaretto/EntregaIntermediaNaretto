from django.db import models

# Create your models here.

class Gerencia(models.Model):
    nombre=models.CharField(max_length=40)
    n_integrantes = models.IntegerField()

    def __str__(self):
        return f"Gerencia: {self.nombre} - Numero de Integrantes: {self.n_integrantes}"

class Gerente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    gerencia= models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Gerencia {self.gerencia}"

class Colaborador(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    cargo= models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Cargo {self.cargo}"
