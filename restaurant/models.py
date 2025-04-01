from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Kategoriename

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    PRICE_CHOICES = [
        ('$', 'Günstig'),
        ('$$', 'Mittelpreisig'),
        ('$$$', 'Teuer'),
    ]

    name = models.CharField(max_length=100)  # Name des Restaurants
    description = models.TextField()         # Beschreibung des Restaurants
    price = models.CharField(max_length=3, choices=PRICE_CHOICES)  # Preis als Symbol
    categories = models.ManyToManyField(Category, related_name='restaurants')  # Verknüpfung mit Kategorien
    image = models.ImageField(upload_to='restaurant_images/', blank=True, null=True)  # Bild-Upload
    phone = models.CharField(max_length=20, blank=True, null=True)  # Telefonnummer
    address = models.CharField(max_length=255, blank=True, null=True)  # Adresse
    opening_hours = models.TextField(blank=True, null=True)  # Öffnungszeiten
    website = models.URLField(blank=True, null=True)  # Website-URL

    def __str__(self):
        return self.name
