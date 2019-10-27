import datetime

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.core.exceptions import ImproperlyConfigured
from django.db.models import Sum
from django.http import Http404

from automoney.models import Venda, Compra


class HomePageView(TemplateView):
	template_name = "automoney/index.html"

class VendaListView(ListView):
	model = Venda
	template_name = 'automoney/listvenda.html'
	date_field = "data"
	date_format = '%Y-%m-%d'
	since_date = None
	until_date = None
	auto_until_date = False

	def get_date_field(self):
		if self.date_field is None:
			raise ImproperlyConfigured("%s.date_field is required." % self.__class__.__name__)
		return self.date_field

	def get_date_format(self):
		return self.date_format

	def get_since_date(self):
		since_date = self.since_date
		if since_date is None:
			try:
				since_date = self.kwargs['since']
			except KeyError:
				try:
					since_date = self.request.GET['since']
				except KeyError:
					raise Http404("No since date specified")
		format = self.get_date_format()
		return datetime.datetime.strptime(since_date, format).date()

	def get_until_date(self):
		until_date = self.until_date
		if until_date is None:
			try:
				until_date = self.kwargs['until']
			except KeyError:
				try:
					until_date = self.request.GET['until']
				except KeyError:
					if self.auto_until_date:
						return self.get_until_date_from_since_date()
					else:
						raise Http404("No until date specified")
		format = self.get_date_format()
		return datetime.datetime.strptime(until_date, format).date()

	def get_until_date_from_since_date(self):
		if self.auto_until_date:
			raise NotImplementedError("If auto_util_date=True, get_until_date_from_since_date must be implemented")

	def get_queryset(self):
		queryset = super(VendaListView, self).get_queryset()
		date_field = self.get_date_field()
		since = self.get_since_date()
		until = self.get_until_date()
		lookup_kwargs = {
			'%s__gte' % date_field: since,
			'%s__lt' % date_field: until,
		}
		queryset = queryset.filter(**lookup_kwargs).order_by('-%s' % date_field)
		return queryset

	def get_total(self):
		total = self.get_queryset().aggregate(total=Sum('valortotal')).get('total')
		return total

	def get_context_data(self, **kwargs):
		context = {'total': self.get_total(),
				   'since': self.get_since_date(),
				   'until': self.get_until_date()}
		context.update(kwargs)
		return super(VendaListView, self).get_context_data(**context)


class CompraListView(ListView):
	model = Compra
	template_name = 'automoney/listcompra.html'
	date_field = "data"
	date_format = '%Y-%m-%d'
	since_date = None
	until_date = None
	auto_until_date = False

	def get_date_field(self):
		if self.date_field is None:
			raise ImproperlyConfigured("%s.date_field is required." % self.__class__.__name__)
		return self.date_field

	def get_date_format(self):
		return self.date_format

	def get_since_date(self):
		since_date = self.since_date
		if since_date is None:
			try:
				since_date = self.kwargs['since']
			except KeyError:
				try:
					since_date = self.request.GET['since']
				except KeyError:
					raise Http404("No since date specified")
		format = self.get_date_format()
		return datetime.datetime.strptime(since_date, format).date()

	def get_until_date(self):
		until_date = self.until_date
		if until_date is None:
			try:
				until_date = self.kwargs['until']
			except KeyError:
				try:
					until_date = self.request.GET['until']
				except KeyError:
					if self.auto_until_date:
						return self.get_until_date_from_since_date()
					else:
						raise Http404("No until date specified")
		format = self.get_date_format()
		return datetime.datetime.strptime(until_date, format).date()

	def get_until_date_from_since_date(self):
		if self.auto_until_date:
			raise NotImplementedError("If auto_util_date=True, get_until_date_from_since_date must be implemented")

	def get_queryset(self):
		queryset = super(CompraListView, self).get_queryset()
		date_field = self.get_date_field()
		since = self.get_since_date()
		until = self.get_until_date()
		lookup_kwargs = {
			'%s__gte' % date_field: since,
			'%s__lt' % date_field: until,
		}
		queryset = queryset.filter(**lookup_kwargs).order_by('-%s' % date_field)
		return queryset

	def get_total(self):
		total = self.get_queryset().aggregate(total=Sum('valortotal')).get('total')
		return total

	def get_context_data(self, **kwargs):
		context = {'total': self.get_total(),
				   'since': self.get_since_date(),
				   'until': self.get_until_date()}
		context.update(kwargs)
		return super(CompraListView, self).get_context_data(**context)

class BalancoListView(ListView):
	template_name = 'automoney/listbalanco.html'
	date_field = "data"
	date_format = '%Y-%m-%d'
	since_date = None
	until_date = None
	auto_until_date = False

	def get_date_field(self):
		if self.date_field is None:
			raise ImproperlyConfigured("%s.date_field is required." % self.__class__.__name__)
		return self.date_field

	def get_date_format(self):
		return self.date_format

	def get_since_date(self):
		since_date = self.since_date
		if since_date is None:
			try:
				since_date = self.kwargs['since']
			except KeyError:
				try:
					since_date = self.request.GET['since']
				except KeyError:
					raise Http404("No since date specified")
		format = self.get_date_format()
		return datetime.datetime.strptime(since_date, format).date()

	def get_until_date(self):
		until_date = self.until_date
		if until_date is None:
			try:
				until_date = self.kwargs['until']
			except KeyError:
				try:
					until_date = self.request.GET['until']
				except KeyError:
					if self.auto_until_date:
						return self.get_until_date_from_since_date()
					else:
						raise Http404("No until date specified")
		format = self.get_date_format()
		return datetime.datetime.strptime(until_date, format).date()

	def get_until_date_from_since_date(self):
		if self.auto_until_date:
			raise NotImplementedError("If auto_util_date=True, get_until_date_from_since_date must be implemented")

	def get_queryset(self):
		date_field = self.get_date_field()
		since = self.get_since_date()
		until = self.get_until_date()
		lookup_kwargs = {
			'%s__gte' % date_field: since,
			'%s__lt' % date_field: until,
		}
		queryset = {'compras': Compra.objects.filter(**lookup_kwargs).order_by('-%s' % date_field),
					'vendas': Venda.objects.filter(**lookup_kwargs).order_by('-%s' % date_field)}
		return queryset

	def get_compras(self):
		totalcompras = self.get_queryset()['compras'].aggregate(total=Sum('valortotal')).get('total') or 0
		return totalcompras

	def get_vendas(self):
		totalvendas = self.get_queryset()['vendas'].aggregate(total=Sum('valortotal')).get('total') or 0
		return totalvendas

	def get_balanco(self):
		balanco = self.get_vendas() - self.get_compras()
		return balanco

	def get_context_data(self, **kwargs):
		context = {'totalcompras': self.get_compras(),
				   'totalvendas': self.get_vendas(),
				   'balanco': self.get_balanco(),
				   'since': self.get_since_date(),
				   'until': self.get_until_date()}
		context.update(kwargs)
		return super(BalancoListView, self).get_context_data(**context)