from django.urls import path

from .views import HomePageView, VendaListView

urlpatterns = [
	path('', HomePageView.as_view(), name='index'),
	path('venda/', VendaListView.as_view(), name='venda'),
]