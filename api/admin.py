from django.contrib import admin
from .models import Usuario, Peluqueria, Servicio, Empleado, Reserva

admin.site.register(Usuario)
admin.site.register(Peluqueria)
admin.site.register(Servicio)
admin.site.register(Empleado)
admin.site.register(Reserva)