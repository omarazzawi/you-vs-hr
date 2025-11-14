from django.contrib import admin
from .models import Story, Comment
# Register your models here.

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'story', 'created_at', 'approved']
    list_filter = ['approved', 'created_at']
    search_fields = ['content', 'author__username']
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        
        count = queryset.update(approved=True)
        self.message_user(request, f"{count} comment(s) approved successfully.")
    approve_comments.short_description = "Approve selected comments"