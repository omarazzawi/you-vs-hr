from django.contrib import admin
from .models import Page, ResourceCategory, Resource


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Admin configuration for Page model."""

    list_display = ['title', 'slug', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'content')
        }),
        ('About/Policy Sections', {
            'fields': (
                'mission', 'guidelines', 'privacy_policy', 'terms_of_use'
            ),
            'description': 'These fields are for the About & Policy page'
        }),
    )


@admin.register(ResourceCategory)
class ResourceCategoryAdmin(admin.ModelAdmin):
    """Admin configuration for ResourceCategory model."""

    list_display = ['name', 'order', 'icon']
    list_editable = ['order']


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    """Admin configuration for Resource model."""

    list_display = ['title', 'category', 'order', 'active']
    list_filter = ['category', 'active']
    list_editable = ['order', 'active']
    search_fields = ['title', 'description']
