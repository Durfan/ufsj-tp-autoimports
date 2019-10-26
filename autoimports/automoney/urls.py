from django.urls import path

from .views import HomePageView, VendasMonthView, VendaListView

urlpatterns = [
	path('', HomePageView.as_view(), name='index'),
	path('venda/', VendaListView.as_view(), name='venda'),
	path('<int:year>/<int:month>/',
		VendasMonthView.as_view(month_format='%m'),
		name="archive_month_numeric"),
]