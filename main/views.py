from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
def main(request):
    data = [1, 1, 1]

    return JsonResponse(data, safe=False)