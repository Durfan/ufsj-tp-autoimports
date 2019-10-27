from django.urls import path

from .views import HomePageView, VendaListView, CompraListView, BalancoListView

urlpatterns = [
	path('', HomePageView.as_view(), name='index'),
	path('venda/', VendaListView.as_view(), name='venda'),
	path('compra/', CompraListView.as_view(), name='compra'),
	path('balanco/', BalancoListView.as_view(), name='balanco'),
]