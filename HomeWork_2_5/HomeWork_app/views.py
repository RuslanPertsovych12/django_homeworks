from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
import random

# Create your views here.
def products_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def replenish(request, count):
    names = ['Молоток', 'Викрутка', 'Дриль']
    tool_types = ['Ручний', 'Ручна', 'Електрична']
    brands = ['Bosch', 'Makita', 'Stanley', 'DeWalt', 'Hitachi']

    for _ in range(count):
        Product.objects.create(
            name=random.choice(names),
            tool_type=random.choice(tool_types),
            weight_kg=round(random.uniform(0.3, 2.0), 2),
            brand=random.choice(brands),
            price=round(random.uniform(50, 2000), 2)
        )
    return HttpResponse(f"Додано {count} нових записів")
