from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)  # Name des Restaurants
    description = models.TextField()         # Beschreibung des Restaurants
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preis
    category = models.CharField(max_length=100)  # Kategorie (z. B. Fast Food, Fine Dining, etc.)

    def __str__(self):
        return self.name
