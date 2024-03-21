from django.http import JsonResponse
from django.shortcuts import render
from geopy.distance import geodesic

import main.core.add_shipment as add_shipment_func
# Create your views here.

from main.models import *
def main(request):
    data = [1, 1, 1]

    return JsonResponse(data, safe=False)

def add_shipment(request):
    """
        Данная функция добавляет новый груз (add_shipment_func), следуя правилам:
        - Создание нового груза (характеристики локаций pick-up, delivery определяются по введенному zip-коду);

        Запрос должен содержать zip_code, weight и description.
        Запрос может быть как GET так и POST.
    """
    if request.method == 'GET':
        zip_code = request.GET.get('zip_code')
        weight = request.GET.get('weight')
        description = request.GET.get('description')
    elif request.method == 'POST':
        zip_code = request.POST.get('zip_code')
        weight = request.POST.get('weight')
        description = request.POST.get('description')
    else:
        return JsonResponse('Проблема с сервером. Запрос должен быть GET или POST,')
    if  zip_code and weight and description:
        # Получение локации
        location = Location.objects.get(zip_code="12345")

        # Добавление в БД
        """
            Так как не было уточнения конкретно для чего служит pick_up и delivery, они создаются на одной точнке локации.
        """
        shipment = Shipment.objects.create(
            loc_pick_up=location,
            loc_delivery=location,
            weight=weight,
            description=description,
        )

        shipment.save()

    return JsonResponse('Груз был добавлен.')
