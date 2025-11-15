from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('story/create/', views.create_story, name='create_story'), #<<< ALWAYS Story/create/ must come BEFORE story/<slug:slug>/
    path('story/<slug:slug>/', views.story_detail, name='story_detail'),
]