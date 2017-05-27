from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/', views.login, name='login'),
	url(r'^logout/', views.logout, name='logout'),
	url(r'^add/', views.add, name='add'),
	url(r'^edit/([0-9]+)', views.edit, name='edit'),
	url(r'^view/([0-9]+)', views.view, name='view'),
	url(r'^delete/([0-9]+)', views.delete, name='delete'),
	url(r'^registration/', views.registration, name='registration'),
]
