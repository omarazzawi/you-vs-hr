from django.contrib import admin
from .models import Page
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'content')
        }),
        ('About/Policy Sections', {
            'fields': ('mission', 'guidelines', 'privacy_policy', 'terms_of_use'),
            'description': 'These fields are for the About & Policy page'
        }),
    )