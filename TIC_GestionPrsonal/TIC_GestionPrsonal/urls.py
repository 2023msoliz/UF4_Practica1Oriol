from django.contrib import admin
from django.urls import path
from centre import views

urlpatterns = [
    path('centre/teachers/', views.teachers, name='teachers'),
]
