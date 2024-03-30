from django.urls import path
from . import views

urlpatterns = [
    path('soilParameters/add/', views.add_parameters),
    path('soilParameters/all/', views.get_parameters),
    path('soilParameters/download/', views.download_csv),
]
