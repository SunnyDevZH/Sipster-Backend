from django.contrib import admin
from .models import Restaurant, Category  # Importiere das Category-Modell

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'phone', 'address', 'website', 'get_categories', 'image_preview']  # Zusätzliche Felder in der Liste
    fields = [
        'name', 'price', 'description', 'categories', 'image', 
        'phone', 'address', 'opening_hours', 'website'  # Zusätzliche Felder im Bearbeitungsformular
    ]
    filter_horizontal = ['categories']  # Aktiviert eine Mehrfachauswahl für Kategorien

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'  # Spaltenname im Admin-Bereich

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 50px; height: 50px;" />'
        return "Kein Bild"
    image_preview.allow_tags = True
    image_preview.short_description = 'Bildvorschau'

# Registriere das Category-Modell
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']  # Zeigt den Namen der Kategorie im Admin-Bereich an
