from django.contrib import admin
from django.contrib import messages
# Register your models here.
from base.models import Contato


@admin.action(description='Marca formulario(s) de contato como lido(s)')
def marcar_como_lido(modeladmin, request, queryset):
    queryset.update(lido=True)
    modeladmin.message_user(request, 'Formulario(s) de Contato marcado(s) como lido(s)', messages.SUCCESS)
    
    
@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'data', 'lido']
    search_fields = ['nome', 'email']
    list_fields = ['data', 'lido']
    actions = [marcar_como_lido]