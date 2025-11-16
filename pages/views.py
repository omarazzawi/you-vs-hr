from django.shortcuts import render, get_list_or_404
from .models import Page
# Create your views here.


def about_page(request):
    """Display About & Policies page"""
    page = get_object_or_404(Page, slug='about-policies')
    return render(request, 'pages/about.html', {'page': page})