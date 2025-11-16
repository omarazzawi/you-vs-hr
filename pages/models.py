from django.db import models

# Create your models here.

class Page(models.Model):
    """Model for static pages with editable content"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(help_text="Main page content")
    
    # For About/Policy page sections
    mission = models.TextField(blank=True, help_text="Mission statement")
    guidelines = models.TextField(blank=True, help_text="Community guidelines")
    privacy_policy = models.TextField(blank=True, help_text="Privacy policy")
    terms_of_use = models.TextField(blank=True, help_text="Terms of use")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title
