from django.contrib import admin
from .models import Income

class IncomeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Income, IncomeAdmin)
