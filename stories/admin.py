from django.contrib import admin
from .models import Story, Comment


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    """Admin configuration for Story model."""

    list_display = ['title', 'slug', 'author', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin configuration for Comment model."""

    list_display = ['author', 'story', 'created_at', 'approved']
    list_filter = ['approved', 'created_at']
    search_fields = ['content', 'author__username']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """Approve selected comments in bulk."""
        count = queryset.update(approved=True)
        self.message_user(
            request, f"{count} comment(s) approved successfully."
        )
    approve_comments.short_description = "Approve selected comments"
