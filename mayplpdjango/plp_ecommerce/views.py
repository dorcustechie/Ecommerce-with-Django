# from django.shortcuts import render
from django.http import httpResponse

# Create your views here.
def index(request):
    return httpResponse("My first webpage with python Django")
