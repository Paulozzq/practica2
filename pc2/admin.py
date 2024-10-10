from django.contrib import admin

from .models import Marca, Modelo, Producto

# Registrar los modelos en el panel de administración
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Producto)