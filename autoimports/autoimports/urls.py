from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from django.views.generic.base import TemplateView

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='staticpage/home.html'), name='home'),
	path('automoney/', include('automoney.urls')),
	path('admin/', admin.site.urls),
	path('accounts/', include('django.contrib.auth.urls')),
]
