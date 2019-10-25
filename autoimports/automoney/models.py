from django.db import models

class Equipamento(models.Model):
	nome = models.CharField(max_length=254)
	cor = models.CharField(max_length=128)
	descricao = models.TextField()
	quantidade = models.IntegerField()
	valorcompra = models.DecimalField(max_digits=19, decimal_places=2)
	valovenda = models.DecimalField(max_digits=19, decimal_places=2)
	logistica = models.BooleanField()

	class Meta:
		db_table = 'equipamento'

	def __str__(self):
		return self.nome


class Compra(models.Model):
	data = models.DateTimeField()
	equip = models.ForeignKey('Equipamento', on_delete=models.DO_NOTHING)

	class Meta:
		db_table = 'compra'


class Venda(models.Model):
	data = models.DateTimeField()
	equip = models.IntegerField()

	class Meta:
		db_table = 'venda'


