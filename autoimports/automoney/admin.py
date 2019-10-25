from django.contrib import admin

from .models import Equipamento, Compra, Venda

class EquipamentoAdmin(admin.ModelAdmin):
	model = Equipamento
	list_display = ('nome', 'cor', 'quantidade', 'logistica')

admin.site.register(Equipamento, EquipamentoAdmin)

class CompraAdmin(admin.ModelAdmin):
	model = Compra
	list_display = ['data', 'quantidade', 'get_name', 'get_vcompra']

admin.site.register(Compra, CompraAdmin)

class VendaAdmin(admin.ModelAdmin):
	model = Venda
	list_display = ['data', 'quantidade', 'get_name', 'get_vvenda']

admin.site.register(Venda, VendaAdmin)
