"""
Módulo que maneja el administrador de Django, es
utilizdo para manejar los modelos relacionados a
la base de datos.
"""

from django.contrib import admin
from alchemy.models import *

# Registro de modelos que usaremos de la BD
admin.site.register(Elementos)
admin.site.register(Mezclas)
