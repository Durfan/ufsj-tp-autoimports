from django.contrib import admin

from .models import Equipamento, Compra, Venda

admin.site.register(Equipamento)
admin.site.register(Compra)
admin.site.register(Venda)
