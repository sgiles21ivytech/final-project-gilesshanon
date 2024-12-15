from django.conf import settings
from django.db import models

class MenuItem(models.Model):
    menuID = models.IntegerField(primary_key=True)  # Assuming integer-based menu IDs
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # Allow for optional descriptions
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Accommodate prices with decimals

    def __str__(self):
        return f"{self.menuID}: {self.name}"  # Clear and informative representation


    def get_total_price(self, quantity=1):
        return self.price * quantity  # Calculate total price based on quantity
