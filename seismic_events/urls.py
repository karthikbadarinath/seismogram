from . import views
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title  = settings.ADMIN_SITE_TITLE

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add/', views.add, name='add'),
	url(r'^edit/([0-9]+)', views.edit, name='edit'),
	url(r'^view/([0-9]+)', views.view, name='view'),
	url(r'^delete/([0-9]+)', views.delete, name='delete'),
]
