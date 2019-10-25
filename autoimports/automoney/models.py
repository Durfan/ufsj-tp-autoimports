from django.db import models


class Equipamento(models.Model):
	nome = models.CharField(max_length=254)
	cor = models.CharField(max_length=128)
	descricao = models.TextField("Descrição")
	quantidade = models.IntegerField()
	valorcompra = models.DecimalField("Valor de Compra", max_digits=19, decimal_places=2)
	valorvenda = models.DecimalField("Valor de Venda", max_digits=19, decimal_places=2)
	logistica = models.BooleanField("Requer Compra")

	class Meta:
		db_table = 'equipamento'

	def __str__(self):
		return self.nome


class Compra(models.Model):
	data = models.DateTimeField()
	quantidade = models.IntegerField()
	equip = models.ForeignKey('Equipamento', models.DO_NOTHING, verbose_name="Equipamento")

	class Meta:
		db_table = 'compra'

	def __str__(self):
		return self.equip.nome

	def get_name(self):
		return self.equip.nome

	def get_vcompra(self):
		return self.equip.valorcompra

	get_name.short_description = 'Equipamento'
	get_vcompra.short_description = 'Valor da Compra'


class Venda(models.Model):
	data = models.DateTimeField()
	quantidade = models.IntegerField()
	equip = models.ForeignKey('Equipamento', models.DO_NOTHING, verbose_name="Equipamento")

	class Meta:
		db_table = 'venda'

	def __str__(self):
		return self.equip.nome

	def get_name(self):
		return self.equip.nome

	def get_vvenda(self):
		return self.equip.valorvenda

	get_name.short_description = 'Equipamento'
	get_vvenda.short_description = 'Valor da Venda'
