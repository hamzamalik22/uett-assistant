from django.urls import path
from . import views

urlpatterns = [
    path('titlepage/', views.generate_pdf, name='generate_pdf'),
]
