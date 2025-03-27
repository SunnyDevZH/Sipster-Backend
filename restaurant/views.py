from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantListView(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True, context={'request': request})
        return Response(serializer.data)
