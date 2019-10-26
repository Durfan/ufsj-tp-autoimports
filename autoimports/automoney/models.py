from django.db import models


class Equipamento(models.Model):
	nome = models.CharField(max_length=254)
	cor = models.CharField(max_length=128)
	descricao = models.TextField("Descrição")
	quantidade = models.IntegerField()
	logistica = models.BooleanField("Requer Compra")

	class Meta:
		db_table = 'equipamento'

	def __str__(self):
		return self.nome


class Compra(models.Model):
	data = models.DateTimeField()
	quantidade = models.IntegerField()
	valorunico = models.DecimalField("Valor unitario",  max_digits=19, decimal_places=2)
	valortotal = models.DecimalField("Valor da Compra", max_digits=19, decimal_places=2)
	equip = models.ForeignKey('Equipamento', models.DO_NOTHING, verbose_name="Equipamento")

	class Meta:
		db_table = 'compra'

	def __str__(self):
		return self.equip.nome

	def get_name(self):
		return self.equip.nome

	get_name.short_description = 'Equipamento'


class Venda(models.Model):
	data = models.DateTimeField()
	quantidade = models.IntegerField()
	valorunico = models.DecimalField("Valor unitario", max_digits=19, decimal_places=2)
	valortotal = models.DecimalField("Valor da Venda", max_digits=19, decimal_places=2)
	equip = models.ForeignKey('Equipamento', models.DO_NOTHING, verbose_name="Equipamento")

	class Meta:
		db_table = 'venda'

	def __str__(self):
		return self.equip.nome

	def get_name(self):
		return self.equip.nome

	get_name.short_description = 'Equipamento'
