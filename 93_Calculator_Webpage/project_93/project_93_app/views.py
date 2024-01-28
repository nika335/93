from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def add(request, num_1, num_2):
    return HttpResponse(f"{num_1 + num_2}")

def subtract(request, num_1, num_2):
    return HttpResponse(f"{num_1 - num_2}")

def multiply(request, num_1, num_2):
    return HttpResponse(f"{num_1 * num_2}")

def divide(request, num_1, num_2):
    return HttpResponse(f"{num_1 - num_2}")