from django.db import models

# Create your models here.
class Product(models.Model):
    TOOL_CHOICES = [
        ('Молоток', 'Молоток'),
        ('Викрутка', 'Викрутка'),
        ('Дриль', 'Дриль'),
    ]

    name = models.CharField(max_length=50, choices=TOOL_CHOICES)
    tool_type = models.CharField(max_length=50)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.brand})"
