from django.shortcuts import render
from django.http import JsonResponse
from .operations import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

"""def from_decimal(request):
    return render(request, 'from-decimal.html')

def to_decimal(request):
    return render(request, 'to-decimal.html')

def add_two_numbers(request):
    return render(request, 'add-two-numbers.html')"""