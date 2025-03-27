from django.db import models

class Restaurant(models.Model):
    PRICE_CHOICES = [
        ('$', 'Günstig'),
        ('$$', 'Mittelpreisig'),
        ('$$$', 'Teuer'),
    ]

    name = models.CharField(max_length=100)  # Name des Restaurants
    description = models.TextField()         # Beschreibung des Restaurants
    price = models.CharField(max_length=3, choices=PRICE_CHOICES)  # Preis als Symbol
    category = models.CharField(max_length=100)  # Kategorie (z. B. Fast Food, Fine Dining, etc.)
    image = models.ImageField(upload_to='restaurant_images/', blank=True, null=True)  # Bild-Upload

    def __str__(self):
        return self.name
