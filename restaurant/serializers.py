from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'description', 'price', 'category', 'image']

    def get_image(self, obj):
        request = self.context.get('request')  # Kontext abrufen
        if obj.image:
            return request.build_absolute_uri(obj.image.url)  # Absolute URL generieren
        return None