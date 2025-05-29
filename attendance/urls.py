from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_attendance, name='calculate_attendance'),
]
