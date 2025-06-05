from django.contrib import admin
from django.utils.html import format_html
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'price', 'description', 'phone', 'address', 'website',
        'get_categories', 'image_preview'
    ]
    fields = [
        'name', 'price', 'description', 'categories', 'image',
        'phone', 'address', 'opening_hours', 'website'
    ]
    filter_horizontal = ['categories']  # WICHTIG: für ManyToMany-Feld

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Kategorien'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return "Kein Bild"
    image_preview.short_description = 'Bildvorschau'
