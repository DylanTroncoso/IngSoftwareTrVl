import datetime
from django.db import models

# Create your models here.

class Servicio(models.Model):
    idServicio = models.AutoField(primary_key=True, default=1)
    nombre = models.CharField(max_length=50, default='Nombre del servicio')
    precio = models.IntegerField(default=10000)
    descripcion = models.TextField(default='Descripción del servicio')
    stock = models.IntegerField(default=10)
    imagen = models.ImageField(upload_to='servicios', null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} (ID: {self.idServicio})'
    
class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    total = models.BigIntegerField()
    fechaCompra = models.DateTimeField(blank=False, null=False, default= datetime.datetime.now)

    def __str__(self):
        return str(self.id_boleta)
    
class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)
