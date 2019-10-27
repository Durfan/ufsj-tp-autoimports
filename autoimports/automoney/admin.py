from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Employee, Equipamento, Compra, Venda

class EmployeeInline(admin.StackedInline):
	model = Employee
	can_delete = False
	verbose_name_plural = 'employee'

class UserAdmin(BaseUserAdmin):
	inlines = (EmployeeInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class EquipamentoAdmin(admin.ModelAdmin):
	model = Equipamento
	list_display = ('nome', 'cor', 'quantidade', 'logistica')

admin.site.register(Equipamento, EquipamentoAdmin)

class CompraAdmin(admin.ModelAdmin):
	model = Compra
	list_display = ['data', 'quantidade', 'get_name', 'valorunico', 'valortotal']

admin.site.register(Compra, CompraAdmin)

class VendaAdmin(admin.ModelAdmin):
	model = Venda
	list_display = ['data', 'quantidade', 'get_name', 'valorunico', 'valortotal']

admin.site.register(Venda, VendaAdmin)
