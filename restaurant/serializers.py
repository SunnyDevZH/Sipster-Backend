from rest_framework import serializers
from .models import Restaurant, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class RestaurantSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)  # Mehrere Kategorien serialisieren
    image = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'description', 'price', 'categories', 'image']

    def get_image(self, obj):
        request = self.context.get('request')  # Kontext abrufen
        if obj.image:
            return request.build_absolute_uri(obj.image.url)  # Absolute URL generieren
        return None