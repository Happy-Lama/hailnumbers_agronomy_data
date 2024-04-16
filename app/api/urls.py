# 16/04/2001: added url for retrieving modules and to get module parameters

from django.urls import path
from . import views

urlpatterns = [
    path('soilParameters/add/', views.add_parameters),
    path('soilParameters/<str:module_id>/', views.get_parameters),
    path('soilParameters/download/', views.download_csv),
    path('soilParameters/modules/all/', views.get_modules),
]
