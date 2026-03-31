from django.contrib import admin
from .models import Restaurante, Pedido, Producto

admin.site.register(Restaurante)
admin.site.register(Pedido)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('restaurante', 'nombre', 'precio')
    ordering = ('precio', )
    search_fields = ('nombre',)
    list_filter = ('restaurante',)

admin.site.register(Producto, ProductoAdmin)