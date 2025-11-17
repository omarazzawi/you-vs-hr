from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # Story URLs - SPECIFIC paths BEFORE slug pattern
    path('story/create/', views.create_story, name='create_story'),
    path('story/<slug:slug>/edit/', views.edit_story, name='edit_story'),
    path('story/<slug:slug>/delete/', views.delete_story, name='delete_story'),
    # Story detail - keep slug pattern last to avoid conflicts
    path('story/<slug:slug>/', views.story_detail, name='story_detail'),
    # Comment URLs
    path('comment/<int:comment_id>/edit/', views.edit_comment,
         name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment,
         name='delete_comment'),
]
