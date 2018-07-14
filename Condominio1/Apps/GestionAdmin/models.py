from django.db import models

# Create your models here.

class Proveedor(models.Model):
    Rut = models.PositiveIntegerField()
    Dig = models.CharField(max_length=1)
    Nombre = models.CharField(max_length=35)
    Estado = models.BooleanField(default=True)

    #def RutC(self):
    #    cadena="{0}, {1}, {2}"
    #    Rutcar= str(self.Rut)
    #    return cadena.format(Rutcar, self.Dig)

    #def __str__(self):
    #    return self.RutC

class Rubro(models.Model):
    Codigo = models.PositiveIntegerField()
    Descripcion= models.CharField(max_length=25)
    TIPOS = (('I', 'Ingreso'), ('G', 'Gasto'))
    Tipo = models.CharField(max_length=1, choices=TIPOS, default='I')

    def __str__(self):
        return "{0} ({1})".format(self.Codigo, self.Descripcion)

class Gasto(models.Model):
    Proveedor=models.ForeignKey(Proveedor, null=False, blank=False, on_delete=models.CASCADE)
    Rubro= models.ForeignKey(Rubro, null=False, blank=False, on_delete=models.CASCADE)
    CodGas= models.PositiveIntegerField()
    DesGas= models.CharField(max_length=20)
    FecGas= models.DateTimeField(auto_now_add=True)
    FecDocGas = models.DateTimeField()
    ValGas = models.PositiveIntegerField()
