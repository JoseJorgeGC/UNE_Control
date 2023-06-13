from django.db import models

# Create your models here.
class Circuitos(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 12, null = False)
    descripcion = models.TextField(max_length = 512)
    balance_deficit = models.FloatField()
    numero_de_afectaciones = models.IntegerField()
    ultima_afectacion = models.DateField(blank = True, null = True)

    def __str__(self):
        return f"{self.nombre}"
    
class Afectaciones(models.Model):
    id = models.AutoField(primary_key = True)
    circuito = models.ForeignKey(Circuitos, on_delete = models.CASCADE)
    fecha = models.DateField()
    hora_afectacion = models.DateTimeField()
    hora_restablecido = models.DateTimeField()
    tiempo_de_afectacion = models.TimeField()

    def __str__(self):
        return f"{self.circuito} - {self.tiempo_de_afectacion} ({self.fecha})"

class Logs(models.Model):
    id = models.AutoField(primary_key = True)
    circuito = models.ForeignKey(Circuitos, on_delete = models.CASCADE)
    afectado = models.BooleanField()
    descripcion = models.TextField(max_length = 512)
    mw_afectados_en_provincia = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return f"{self.circuito} {self.afectado} - {self.fecha}"

class Estado_SEN(models.Model):
    id = models.AutoField(primary_key = True)
    fecha = models.DateField()
    prevision_de_afectacion = models.IntegerField()
    afectacion_real = models.IntegerField()
    tiempo_de_afectacion = models.IntegerField()

    def __str__(self):
        return f"{self.fecha}"