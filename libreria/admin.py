from django.contrib import admin
from .models import Equipo, Mantenimiento, qrcode

admin.site.site_header='Hostpital'

admin.site.register(Equipo)
admin.site.register(Mantenimiento)

# Register your models here.
