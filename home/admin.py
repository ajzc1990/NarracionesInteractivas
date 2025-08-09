from django.contrib import admin
from .models import Usuario, Localidad, Departamento, Provincia, Jardin, Sesion, Cuento, Sesion_Cuento, Pictograma, Palabra, Reporte_General

admin.site.register(Usuario)
admin.site.register(Localidad)
admin.site.register(Departamento)
admin.site.register(Provincia)
admin.site.register(Jardin)
admin.site.register(Sesion)
admin.site.register(Cuento)
admin.site.register(Sesion_Cuento)
admin.site.register(Pictograma)
admin.site.register(Palabra)
admin.site.register(Reporte_General)
