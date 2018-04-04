from django.db import models

# Primer y creo unico modelo va a ser elementos incluye los atributos.

class Elementos(models.Model):
    Nombre_Elemento = models.CharField(max_length = 35)
    Simbolo_Elemento = models.CharField(max_length = 35)
    Informacion_Elemento = models.CharField(max_length = 200)
    Foto_Elemento = models.CharField(max_length = 50)
    Foto_Tarjeta = models.CharField(max_length = 50)

    def Nombre(self):
        cadena = "{0}"
        return cadena.format(self.Nombre_Elemento)

    def Simbolo(self):
        cadena = "{0}"
        return cadena.format(self.Simbolo_Elemento)

    def Informacion(self):
        cadena = "{0}"
        return cadena.format(self.Informacion_Elemento)

    def Ruta_Elemento(self):
        cadena = "{0}"
        return cadena.format(self.Foto_Elemento)

    def Ruta_Tarjeta(self):
        cadena = "{0}"
        return cadena.format(self.Foto_Tarjeta)
