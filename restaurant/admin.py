from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')  # Zeigt diese Felder in der Admin-Liste an
    search_fields = ('name', 'category')         # Ermöglicht die Suche nach Name und Kategorie
