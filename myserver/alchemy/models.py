"""
Módulo de Django que importa los modelos utilizados en la app
"""

from django.db import models

class Elementos(models.Model):
    """Representa un elemento químico.
    
    Attributes:
        Nombre_Elemento (str)= El nombre del elemento.
        Simbolo_Elemento (str)= El símbolo del elemento.
        Informacion_Elemento (str)= Información relacionada al elemento.
        Foto_Elemento (str)= Dirección de la foto del elemento.
        Foto_Tarjeta (str)= Dirección de la tarjeta que representa al elemento.
    """
    Nombre_Elemento = models.CharField(max_length = 35)
    Simbolo_Elemento = models.CharField(max_length = 35)
    Informacion_Elemento = models.CharField(max_length = 200)
    Foto_Elemento = models.CharField(max_length = 50)
    Foto_Tarjeta = models.CharField(max_length = 50)

    def Nombre(self):
        """Función que regresa el nombre del elemento.

        Returns:
            El nombre del elemento.
        """

        cadena = "{0}"
        return cadena.format(self.Nombre_Elemento)

    def Simbolo(self):
        """Función que regresa símbolo del elemento.

        Returns:
            El símbolo del elemento.
        """

        cadena = "{0}"
        return cadena.format(self.Simbolo_Elemento)

    def Informacion(self):
        """Función que regresa información sobre el elemento.

        Returns:
            La información sobre el elemento.
        """

        cadena = "{0}"
        return cadena.format(self.Informacion_Elemento)

    def Ruta_Elemento(self):
        """Función que regresa la ruta al archivo de la foto para el elemento.

        Returns:
            La ruta a la foto del elemento.
        """

        cadena = "{0}"
        return cadena.format(self.Foto_Elemento)

    def Ruta_Tarjeta(self):
        """Función que regresa la ruta al archivo de la tarjeta para el elemento.

        Returns:
            La ruta a la tarjeta del elemento.
        """

        cadena = "{0}"
        return cadena.format(self.Foto_Tarjeta)

    def __str__(self):
        return self.Nombre_Elemento

class Mezclas(models.Model):
    """Representa una mezcla entre dos elementos.
    
    Attributes:
        Nombre_Mezcla (str)= El nombre de la mezcla.
        Elemento1 (str)= Primer elemento que conforma a la mezcla.
        Elemento2 (str)= Segundo elemento que conforma a la mezcla.
        Foto_Mezcla (str)= Dirección de la foto de la mezcla.
    """
    Nombre_Mezcla = models.CharField(max_length = 35)
    Elemento1 = models.CharField(max_length = 35)
    Elemento2 = models.CharField(max_length = 35)
    Foto_Mezcla = models.CharField(max_length = 35)

    def Nombre(self):
        """Función que regresa el nombre de la mezcla.

        Returns:
            El nombre de la mezcla.
        """
        cadena = "{0}"
        return cadena.format(self.Nombre_Mezcla)

    def Elem1(self):
        """Función que regresa el nombre del primer elemento.

        Returns:
            El nombre del elemento.
        """

        cadena = "{0}"
        return cadena.format(self.Elemento1)

    def Elem2(self):
        """Función que regresa el nombre del segundo elemento.

        Returns:
            El nombre del elemento.
        """

        cadena = "{0}"
        return cadena.format(self.Elemento2)

    def Foto(self):
        """Función que regresa el nombre de archivo de la imagen asociada.

        Returns:
            El nombre de archivo.
        """
        cadena = "{0}"
        return cadena.format(self.Foto_Mezcla)

    def __str__(self):
        return self.Nombre_Mezcla
