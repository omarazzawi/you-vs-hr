from django.shortcuts import render, get_object_or_404
from .models import Page, ResourceCategory
# Create your views here.


def about_page(request):
    """Display About & Policies page"""
    page = get_object_or_404(Page, slug='about-policies')
    return render(request, 'pages/about.html', {'page': page})

def resources_page(request):
    """Display Resources page with categorized links"""
    categories = ResourceCategory.objects.prefetch_related('resources').filter(resources__active=True).distinct()
    return render(request, 'pages/resources.html', {'categories': categories})