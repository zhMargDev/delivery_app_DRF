import csv

from django.db import migrations, transaction
from csv import reader

# Модель
from main.models import Location

# Функция для добавления данных из CSV
def add_locations_from_csv(apps, schema_editor):
    with transaction.atomic():
        with open('uszips.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader, None)  # Skip header

            for row in reader:
                # Создать и сохранить объект Location
                location = Location.objects.create(
                  city=row[3],
                  state=row[17],
                  zip_code=row[10],
                  latitude=row[11],
                  longitude=row[12],
                )
                location.save()
# Обработчик миграции
class Migration(migrations.Migration):

  dependencies = [
    ('main', '0003_initial'),
  ]

  operations = [
    migrations.RunPython(add_locations_from_csv),
  ]