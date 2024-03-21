import random, string

from django.db import migrations, transaction
from faker import Faker
from geopy.geocoders import Nominatim

# Модели
from main.models import Car, Location

# Функция для генерации случайной грузоподъемности
def random_carrying_capacity():
  return round(random.uniform(1, 1000), 2)

# Функция для генерации серийного номера
def generate_serial_number(id):
  random_letter = random.choice(string.ascii_uppercase)
  return f"{id}{random_letter}"

# Функция для добавления машин
def add_cars(apps, schema_editor):
    with transaction.atomic():
        fake = Faker()
        geolocator = Nominatim(user_agent="my_app")

        # Получить все локации
        locations = Location.objects.all()

        # Создать 20 машин
        for i in range(20):
            # Выбрать случайную локацию
            location = random.choice(locations)

            # Сгенерировать случайную грузоподъемность
            carrying_capacity = random_carrying_capacity()

            # Сгенерировать серийный номер
            serial_number = generate_serial_number(i + 1000)

            # Получить координаты локации
            address = f"{location.city}, {location.state}"
            coordinates = geolocator.geocode(address).latitude, geolocator.geocode(address).longitude

            try:
              # Создать и сохранить машину
              Car.objects.create(
                current_location=address,
                carrying_capacity=carrying_capacity,
                latitude=coordinates[0],
                longitude=coordinates[1],
                serial_number=serial_number,
              )
            except:
              pass

# Обработчик миграции
class Migration(migrations.Migration):

  dependencies = [
    ('main', 'add_csv_info'),
  ]

  operations = [
    migrations.RunPython(add_cars),
  ]