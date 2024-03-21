from django.http import JsonResponse

from main.models import Shipment, Location


def add_shipment(pick_up, zip_code, weight, description):
    pass