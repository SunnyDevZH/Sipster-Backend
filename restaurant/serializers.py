from rest_framework import serializers
from .models import Restaurant
from categories.models import Category  # <-- Importiere das richtige Modell

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']

class RestaurantSerializer(serializers.ModelSerializer):
    # Für Lesen: verschachtelte Kategorien
    categories = CategorySerializer(many=True, read_only=True)
    # Für Schreiben: akzeptiere IDs
    category_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all(),
        write_only=True,
        source='categories'
    )
    image = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = [
            'id', 'name', 'description', 'price', 'categories', 'category_ids',
            'image', 'phone', 'address', 'opening_hours', 'website'
        ]

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
