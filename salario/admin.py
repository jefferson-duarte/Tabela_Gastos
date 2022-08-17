from django.contrib import admin
from .models import Salario


@admin.register(Salario)
class SalarioAdmin(admin.ModelAdmin):
    list_display = [
        'salario', 'data'
    ]
