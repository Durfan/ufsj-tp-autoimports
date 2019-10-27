from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	matricula = models.CharField("Matricula",max_length=12)


class Equipamento(models.Model):
	nome = models.CharField(max_length=254)
	cor = models.CharField(max_length=128)
	descricao = models.TextField("Descrição")
	quantidade = models.IntegerField(default='0')
	logistica = models.BooleanField("Requer Compra")

	def __str__(self):
		return self.nome


class Compra(models.Model):
	data = models.DateTimeField()
	quantidade = models.IntegerField(default='0')
	valorunico = models.DecimalField("Valor unitario",  max_digits=19, decimal_places=2, default='0')
	valortotal = models.DecimalField("Valor da Compra", max_digits=19, decimal_places=2, default='0')
	equip = models.ForeignKey('Equipamento', models.DO_NOTHING, verbose_name="Equipamento")

	def __str__(self):
		return self.equip.nome

	def get_name(self):
		return self.equip.nome

	get_name.short_description = 'Equipamento'


class Venda(models.Model):
	data = models.DateTimeField()
	quantidade = models.IntegerField(default='0')
	valorunico = models.DecimalField("Valor unitario", max_digits=19, decimal_places=2, default='0')
	valortotal = models.DecimalField("Valor da Venda", max_digits=19, decimal_places=2, default='0')
	equip = models.ForeignKey('Equipamento', models.DO_NOTHING, verbose_name="Equipamento")

	def __str__(self):
		return self.equip.nome

	def get_name(self):
		return self.equip.nome

	get_name.short_description = 'Equipamento'
