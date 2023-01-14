from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(documentos)
class documentos_admin(admin.ModelAdmin):
    list_display = ('id', 'nombre_doc', 'archivo', 'tipo')

@admin.register(rol_usuarios)
class rol_usuarios_admin(admin.ModelAdmin):
    list_display = ('id', 'nombre_rol')

@admin.register(dato_usuarios)
class dato_usuarios_admin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'contrasenia', 'nombres', 'apellidos', 'correo', 'fk_documento', 'fk_rol')

@admin.register(doc_generados)
class doc_generados_admin(admin.ModelAdmin):
    list_display = ('id', 'doc_generado', 'fk_usuario')

@admin.register(modalidades)
class modalidades_admin(admin.ModelAdmin):
    list_display = ('id', 'nombre_modalidad')

@admin.register(rankings)
class rankings_admin(admin.ModelAdmin):
    list_display = ('id', 'ranking')

@admin.register(dato_tutores)
class dato_tutores_admin(admin.ModelAdmin):
    list_display = ('id', 'grado', 'nombres', 'apellidos', 'nro_tutorados', 'ses_individuales', 'ses_grupales', 'referidos', 'atendidos', 'criterio', 'fk_ranking', 'fk_usuario')

@admin.register(dato_tutorados)
class dato_tutorados_admin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'ciclo', 'tipo_beca', 'fk_dato_tutor', 'fk_ranking', 'fk_usuario')