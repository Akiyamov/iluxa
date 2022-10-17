from django.contrib import admin
from .models import ilaksa

# Register your models here.

@admin.register(ilaksa)
class ilaksaAdmin(admin.ModelAdmin):
    list_display = ('name', 'descr', 'date_start', 'status_idea', 'date_finish')
    list_filter = ('status_idea',)