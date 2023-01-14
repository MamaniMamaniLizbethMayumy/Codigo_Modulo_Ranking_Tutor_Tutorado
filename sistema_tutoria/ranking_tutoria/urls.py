from django.urls import path
from ranking_tutoria.views import *
from . import views

urlpatterns = [
	path('login/', inicio_sesion.as_view(), name='inicio_sesion'),
	path('', views.autenticar, name='autenticar'),
	path('', views.mostrar, name='mostrar'),
	path('subir_tutorados/', views.subir_tutorados, name='subir_tutorados'),
	path('mostrar_tutorados/', views.mostrar_tutorados, name='mostrar_tutorados'),
]