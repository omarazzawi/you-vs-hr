from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Test the web"""
    return HttpResponse("Welcome to YouVsHR Stories!")