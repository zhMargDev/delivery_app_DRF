
from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', main),
    path('add_shipment', add_shipment),
]
