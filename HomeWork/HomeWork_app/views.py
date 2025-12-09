from django.shortcuts import render
from django.http import HttpResponse
from .models import InventoryRecord, Product, Warehouse
from django.utils import timezone
import random

# Create your views here.s
def inventory_list(request):
    records = InventoryRecord.objects.select_related('product', 'warehouse').all()
    return render(request, 'inventory_list.html', {'records': records})

def inventory_replenish(request, count):
    products = list(Product.objects.all())
    warehouses = list(Warehouse.objects.all())

    if not products or not warehouses:
        return HttpResponse("❌ У базі немає товарів або складів.")

    created = 0
    updated = 0

    for _ in range(count):
        product = random.choice(products)
        warehouse = random.choice(warehouses)

        record, is_created = InventoryRecord.objects.get_or_create(
            product=product,
            warehouse=warehouse,
            defaults={
                'quantity': random.randint(1, 50),
                'min_required': random.randint(2, 10),
                'last_restock': timezone.now()
            }
        )

        if not is_created:
            record.quantity += random.randint(1, 20)
            record.last_restock = timezone.now()
            record.save()
            updated += 1
        else:
            created += 1

    return HttpResponse(
        f"✅ Створено: {created}, оновлено: {updated}"
    )


def inventory_alerts(request):
    records = InventoryRecord.objects.select_related('product', 'warehouse').all()
    alerts = [r for r in records if r.is_below_minimum()]
    return render(request, 'inventory_alerts.html', {'alerts': alerts})
