from django.db import models

class Curso(models.Model):
    #campo del modelo se llama ahora; son los atributos de la clase; ej el nombre es un str. STR tiene un equivalente en la base de datos(models.Charfield)
    nombre = models.CharField(max_length=164) #equivalente de str
    comision = models.IntegerField() #equivalente de int

class Estudiante(models.Model):
    apellido = models.CharField(max_length= 256)
    nombre = models.CharField(max_length= 256)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    DNI = models.CharField(max_length=32)
    fecha_de_nacimiento = models.DateField()

class Profesor(models.Model):
    apellido = models.CharField(max_length= 256)
    nombre = models.CharField(max_length= 256)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    DNI = models.CharField(max_length=32)
    fecha_de_nacimiento = models.DateField()
    profesion = models.CharField(max_length=128)
    bio = models.TextField()

class Entregable(models.Model):
   nombre = models.CharField(max_length= 256)
   fecha_entrega = models.DateTimeField()
   esta_aprobado = models.BooleanField(default=False)


