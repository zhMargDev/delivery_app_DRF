import string

from django.db import models
from rest_framework.exceptions import ValidationError
from faker import Faker
from geopy.geocoders import Nominatim


class Shipment(models.Model):
    id = models.AutoField(primary_key=True)
    # Локация Pick-up
    loc_pick_up = models.CharField(max_length=255)
    # Локация Delivery
    loc_delivery = models.CharField(max_length=255)
    # Вес (1-1000)
    weight = models.PositiveIntegerField(help_text="Введите вес в диапазоне от 1 до 1000")
    # Описание
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Груз №{self.id}: {self.loc_pick_up} -> {self.loc_delivery}"

# Модель "Машина"
class Car(models.Model):
    # Идентификатор (уникальный номер)
    id = models.AutoField(primary_key=True)
    # Текущая локация
    current_location = models.CharField(max_length=255)
    # Грузоподъемность (в тоннах)
    carrying_capacity = models.DecimalField(max_digits=10, decimal_places=2)
    # Серийный номер 1000-9999 + буква
    serial_number = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.id}{self.serial_number}"

    # Валидация
    def clean(self):
        if not 1 <= self.carrying_capacity <= 1000:
            raise ValidationError("Грузоподъемность должна быть в диапазоне от 1 до 1000.")

# Модель "Локация"
class Location(models.Model):
    # Идентификатор
    id = models.AutoField(primary_key=True)
    # Город
    city = models.CharField(max_length=255)
    # Штат
    state = models.CharField(max_length=2)
    # Почтовый индекс (ZIP)
    zip_code = models.CharField(max_length=10)
    # Широта
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    # Долгота
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"{self.city}, {self.state}"

    def get_location(self):
        """
        Получает координаты по ЗИП коду
        """

        geolocator = Nominatim(user_agent="my-app")
        location = geolocator.geocode(self.zip_code)

        if location:
            self.latitude = location.latitude
            self.longitude = location.longitude
            self.save()

        return location


