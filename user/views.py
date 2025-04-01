from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated



class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
            'birthdate': user.profile.birthdate,  
        })

    def put(self, request):
        user = request.user
        data = request.data

        # Aktualisiere die Benutzerdaten
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)

        # Passwort aktualisieren, falls angegeben
        if 'password' in data and data['password']:
            user.set_password(data['password'])

        user.save()  # Speichere die Änderungen

        return Response({
            'message': 'Profil erfolgreich aktualisiert!',
            'username': user.username,
            'email': user.email,
        }, status=status.HTTP_200_OK)

