from django.contrib import admin

from .models import Producto, Proveedor, Estante, Locker, Mueble, Caja
# Register your models here.

admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Estante)
admin.site.register(Locker)
admin.site.register(Mueble)
admin.site.register(Caja)